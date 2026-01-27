import psycopg2
import argparse
import sys
from typing import List, Optional

# 연결 정보 (create_db.py와 동일한 설정 사용)
rds_host = "nxt-ella-rag-db.cj24wem202yj.us-east-1.rds.amazonaws.com"
db_username = 'postgres'
db_password = '12345678aA'


def get_all_user_databases() -> List[str]:
    """모든 user DB 목록을 가져옵니다 (db_01, db_02, ... 형식)"""
    try:
        conn = psycopg2.connect(
            host=rds_host,
            database='postgres',
            user=db_username,
            password=db_password
        )
        conn.autocommit = True
        
        with conn.cursor() as cursor:
            # db_XX 형식의 데이터베이스만 필터링
            cursor.execute("""
                SELECT datname 
                FROM pg_database 
                WHERE datname ~ '^db_\\d{2}$'
                ORDER BY datname
            """)
            databases = [row[0] for row in cursor.fetchall()]
        
        conn.close()
        return databases
    except Exception as e:
        print(f"데이터베이스 목록 조회 중 오류 발생: {e}")
        sys.exit(1)


def reset_database_data(db_name: str) -> bool:
    """특정 데이터베이스의 모든 테이블 데이터를 삭제합니다 (스키마는 유지)"""
    try:
        db_conn = psycopg2.connect(
            host=rds_host,
            database=db_name,
            user=db_username,
            password=db_password
        )
        db_conn.autocommit = True
        
        with db_conn.cursor() as cursor:
            # 테이블 목록 가져오기
            cursor.execute("""
                SELECT tablename 
                FROM pg_tables 
                WHERE schemaname = 'public'
                ORDER BY tablename
            """)
            tables = [row[0] for row in cursor.fetchall()]
            
            if not tables:
                print(f"  ⚠ {db_name}: 초기화할 테이블이 없습니다.")
                db_conn.close()
                return False
            
            # 시퀀스 목록 가져오기
            cursor.execute("""
                SELECT sequencename 
                FROM pg_sequences 
                WHERE schemaname = 'public'
                ORDER BY sequencename
            """)
            sequences = [row[0] for row in cursor.fetchall()]
            
            # 외래 키 제약 조건을 일시적으로 비활성화 (있는 경우)
            cursor.execute("SET session_replication_role = 'replica';")
            
            # 모든 테이블의 데이터 삭제 (TRUNCATE는 빠르고 시퀀스도 자동 리셋)
            for table in tables:
                try:
                    cursor.execute(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE;')
                    print(f"  ✓ {db_name}.{table}: 데이터 삭제 완료")
                except Exception as e:
                    print(f"  ✗ {db_name}.{table}: 삭제 실패 - {e}")
            
            # 외래 키 제약 조건 다시 활성화
            cursor.execute("SET session_replication_role = 'origin';")
            
            # 시퀀스가 명시적으로 리셋되지 않은 경우를 대비해 리셋
            for sequence in sequences:
                try:
                    cursor.execute(f'ALTER SEQUENCE "{sequence}" RESTART WITH 1;')
                except Exception as e:
                    # 시퀀스 리셋 실패는 무시 (TRUNCATE RESTART IDENTITY로 이미 처리됨)
                    pass
            
            print(f"  ✓ {db_name}: 초기화 완료")
        
        db_conn.close()
        return True
        
    except Exception as e:
        print(f"  ✗ {db_name}: 초기화 중 오류 발생 - {e}")
        return False


def reset_single_database(db_name: str) -> None:
    """단일 데이터베이스 초기화"""
    # DB 존재 여부 확인
    all_dbs = get_all_user_databases()
    
    if db_name not in all_dbs:
        print(f"오류: 데이터베이스 '{db_name}'를 찾을 수 없습니다.")
        print(f"사용 가능한 데이터베이스: {', '.join(all_dbs)}")
        sys.exit(1)
    
    print(f"\n데이터베이스 '{db_name}' 초기화 중...")
    print("⚠️  경고: 모든 데이터가 삭제됩니다. 스키마는 유지됩니다.\n")
    
    success = reset_database_data(db_name)
    
    if success:
        print(f"\n✓ '{db_name}' 초기화가 완료되었습니다.")
    else:
        print(f"\n✗ '{db_name}' 초기화 중 오류가 발생했습니다.")
        sys.exit(1)


def reset_all_databases() -> None:
    """모든 사용자 데이터베이스 초기화"""
    all_dbs = get_all_user_databases()
    
    if not all_dbs:
        print("초기화할 데이터베이스가 없습니다.")
        return
    
    print(f"\n다음 {len(all_dbs)}개의 데이터베이스를 초기화합니다:")
    for db in all_dbs:
        print(f"  - {db}")
    print("\n⚠️  경고: 모든 데이터가 삭제됩니다. 스키마는 유지됩니다.\n")
    
    success_count = 0
    for db_name in all_dbs:
        if reset_database_data(db_name):
            success_count += 1
        print()  # 빈 줄 추가
    
    print(f"\n{'='*50}")
    print(f"초기화 완료: {success_count}/{len(all_dbs)}개 데이터베이스")
    print(f"{'='*50}")


def interactive_mode() -> None:
    """대화형 모드: 사용자가 선택"""
    all_dbs = get_all_user_databases()
    
    if not all_dbs:
        print("초기화할 데이터베이스가 없습니다.")
        return
    
    print("\n삭제 가능한 데이터베이스:")
    for i, db in enumerate(all_dbs, 1):
        print(f"  {i}. {db}")
    print()
    print(f"  {len(all_dbs) + 1}. 전체 초기화")
    print("  0. 취소")
    
    try:
        choice = input("\n선택하세요 (번호 입력): ").strip()
        choice_num = int(choice)
        
        if choice_num == 0:
            print("취소되었습니다.")
            return
        elif choice_num == len(all_dbs) + 1:
            reset_all_databases()
        elif 1 <= choice_num <= len(all_dbs):
            selected_db = all_dbs[choice_num - 1]
            reset_single_database(selected_db)
        else:
            print("잘못된 선택입니다.")
            sys.exit(1)
    except ValueError:
        print("숫자를 입력해주세요.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n취소되었습니다.")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description='데이터베이스 테이블 데이터 초기화 (스키마 유지)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  # 특정 DB 초기화
  python reset_db_data.py --db db_01
  
  # 전체 DB 초기화
  python reset_db_data.py --all
  
  # 대화형 모드
  python reset_db_data.py
        """
    )
    
    parser.add_argument(
        '--db',
        type=str,
        help='초기화할 특정 데이터베이스 이름 (예: db_01)'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='모든 사용자 데이터베이스 초기화'
    )
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='사용 가능한 데이터베이스 목록만 출력'
    )
    
    args = parser.parse_args()
    
    # 연결 정보 확인
    if not rds_host or not db_username or not db_password:
        print("오류: rds_host, db_username, db_password를 설정해주세요.")
        print("파일 상단의 변수를 create_db.py와 동일하게 설정하세요.")
        sys.exit(1)
    
    if args.list:
        all_dbs = get_all_user_databases()
        if all_dbs:
            print("\n사용 가능한 데이터베이스:")
            for db in all_dbs:
                print(f"  - {db}")
        else:
            print("사용 가능한 데이터베이스가 없습니다.")
        return
    
    if args.db:
        reset_single_database(args.db)
    elif args.all:
        reset_all_databases()
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
