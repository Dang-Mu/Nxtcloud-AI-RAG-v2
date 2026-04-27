import boto3
import argparse

### 지워야하는 리소스 키워드 ###
keyword = "kmucd1-"

### 대상 리전 지정 ###
region_name = 'us-east-1'


def delete_iam_role(iam_client, role_name):
    """IAM Role과 연결된 정책 모두 제거 후 Role 삭제"""
    # 인라인 정책 삭제
    try:
        inline = iam_client.list_role_policies(RoleName=role_name)
        for policy_name in inline.get('PolicyNames', []):
            iam_client.delete_role_policy(RoleName=role_name, PolicyName=policy_name)
    except Exception as e:
        print(f"  인라인 정책 삭제 오류 ({role_name}): {e}")

    # 관리형 정책 detach
    try:
        attached = iam_client.list_attached_role_policies(RoleName=role_name)
        for policy in attached.get('AttachedPolicies', []):
            iam_client.detach_role_policy(RoleName=role_name, PolicyArn=policy['PolicyArn'])
    except Exception as e:
        print(f"  관리형 정책 detach 오류 ({role_name}): {e}")

    try:
        iam_client.delete_role(RoleName=role_name)
        print(f"  IAM Role 삭제 완료: {role_name}")
    except Exception as e:
        print(f"  IAM Role 삭제 오류 ({role_name}): {e}")


def delete_s3_bucket(s3_client, s3_resource, bucket_name):
    """S3 버킷 내 객체/버전 모두 삭제 후 버킷 삭제"""
    try:
        print(f"  S3 버킷 비우는 중: {bucket_name}")
        bucket = s3_resource.Bucket(bucket_name)
        bucket.objects.delete()
        bucket.object_versions.delete()
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"  S3 버킷 삭제 완료: {bucket_name}")
    except Exception as e:
        print(f"  S3 버킷 삭제 오류 ({bucket_name}): {e}")


def collect_kb_resources(bedrock_client, kb_list):
    """각 KB에 연결된 data source(S3 버킷)와 IAM Role 수집"""
    resources = []
    for kb in kb_list:
        kb_id = kb['knowledgeBaseId']
        kb_name = kb['name']
        role_arn = kb.get('roleArn', '')
        role_name = role_arn.split('/')[-1] if role_arn else None

        # Data source에서 S3 버킷 목록 수집
        s3_buckets = []
        try:
            paginator = bedrock_client.get_paginator('list_data_sources')
            for page in paginator.paginate(knowledgeBaseId=kb_id):
                for ds in page.get('dataSourceSummaries', []):
                    ds_detail = bedrock_client.get_data_source(
                        knowledgeBaseId=kb_id,
                        dataSourceId=ds['dataSourceId']
                    )
                    s3_cfg = ds_detail.get('dataSource', {}).get('dataSourceConfiguration', {}).get('s3Configuration', {})
                    bucket_arn = s3_cfg.get('bucketArn', '')
                    if bucket_arn:
                        bucket_name = bucket_arn.split(':::')[-1]
                        s3_buckets.append((ds['dataSourceId'], bucket_name))
        except Exception as e:
            print(f"  Data source 조회 오류 ({kb_name}): {e}")

        resources.append({
            'kb_id': kb_id,
            'kb_name': kb_name,
            'role_name': role_name,
            's3_buckets': s3_buckets,
        })
    return resources


def delete_knowledge_bases(keyword, profile_name):
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    bedrock_client = session.client('bedrock-agent')
    iam_client = session.client('iam')
    s3_client = session.client('s3')
    s3_resource = session.resource('s3')

    print("시작\n\n\n")

    # KB 목록 조회 (페이지네이션)
    kb_list = []
    try:
        paginator = bedrock_client.get_paginator('list_knowledge_bases')
        for page in paginator.paginate():
            for kb in page.get('knowledgeBaseSummaries', []):
                if keyword.lower() in kb['name'].lower():
                    kb_detail = bedrock_client.get_knowledge_base(knowledgeBaseId=kb['knowledgeBaseId'])
                    kb_list.append(kb_detail['knowledgeBase'])
    except Exception as e:
        print(f"KB 목록 조회 오류: {e}")
        return

    if not kb_list:
        print("지정된 키워드가 포함된 Knowledge Base를 찾을 수 없습니다.")
        print("\n\n\n종료")
        return

    resources = collect_kb_resources(bedrock_client, kb_list)

    # 삭제 대상 출력
    print("찾은 Knowledge Base 목록:")
    for r in resources:
        print(f"\n[KB] {r['kb_name']} (ID: {r['kb_id']})")
        print(f"  IAM Role : {r['role_name'] or '없음'}")
        if r['s3_buckets']:
            for _, bucket in r['s3_buckets']:
                print(f"  S3 버킷  : {bucket}")
        else:
            print("  S3 버킷  : 없음")

    confirmation = input("\n이 모든 KB / IAM Role / S3 버킷을 삭제하시겠습니까? (y/n): ").strip().lower()

    targets = resources if confirmation == 'y' else []
    if confirmation != 'y':
        for r in resources:
            confirm = input(f"\nKB '{r['kb_name']}'과(와) 연결 리소스를 삭제하시겠습니까? (y/n): ").strip().lower()
            if confirm == 'y':
                targets.append(r)

    for r in targets:
        print(f"\n\n===== 삭제 중: {r['kb_name']} =====")

        # 1. Data source 삭제 (KB 삭제 전 필요)
        for ds_id, _ in r['s3_buckets']:
            try:
                bedrock_client.delete_data_source(knowledgeBaseId=r['kb_id'], dataSourceId=ds_id)
                print(f"  Data source 삭제 완료: {ds_id}")
            except Exception as e:
                print(f"  Data source 삭제 오류 ({ds_id}): {e}")

        # 2. Knowledge Base 삭제
        try:
            bedrock_client.delete_knowledge_base(knowledgeBaseId=r['kb_id'])
            print(f"  Knowledge Base 삭제 완료: {r['kb_name']}")
        except Exception as e:
            print(f"  Knowledge Base 삭제 오류 ({r['kb_name']}): {e}")

        # 3. S3 버킷 삭제
        for _, bucket_name in r['s3_buckets']:
            delete_s3_bucket(s3_client, s3_resource, bucket_name)

        # 4. IAM Role 삭제
        if r['role_name']:
            print(f"  IAM Role 삭제 중: {r['role_name']}")
            delete_iam_role(iam_client, r['role_name'])

    print("\n\n\n종료")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Delete Bedrock Knowledge Bases and associated IAM Roles / S3 buckets.")
    parser.add_argument('-p', '--profile', help="AWS profile name to use.")
    args = parser.parse_args()
    delete_knowledge_bases(keyword, args.profile)
