import os
import io
import json
import time
import uuid
import boto3
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import sys

# shared 모듈 import를 위한 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))
from shared.kb_manager import KBManager

app = FastAPI(
    title="Knowledge Base Admin API",
    description="Knowledge Base 관리를 위한 관리자용 API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# KB Manager 초기화 (파일 경로는 server 실행 위치 기준 또는 절대 경로)
# kbs.json 위치를 server 디렉토리 내에 두거나 shared와 맞추기
KB_FILE_PATH = os.path.join(os.path.dirname(__file__), '../kbs.json')
kb_manager = KBManager(file_path=KB_FILE_PATH)

# AWS 클라이언트 설정
def get_s3_client():
    return boto3.client('s3', region_name="us-east-1")

def get_bedrock_agent_client():
    return boto3.client('bedrock-agent', region_name="us-east-1")

# Pydantic 모델
class ApiResponse(BaseModel):
    status: str
    message: str
    data: Optional[Dict] = None

class KBRegistrationRequest(BaseModel):
    name: str
    kb_id: str
    ds_id: str
    bucket: str
    prefix: Optional[str] = ""

# API 엔드포인트
@app.get("/api/admin/kbs", response_model=ApiResponse)
async def get_kbs():
    try:
        kbs = kb_manager.load_kbs()
        return ApiResponse(
            status="success",
            message="KB 목록 조회 성공",
            data={"kbs": kbs}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/admin/kbs", response_model=ApiResponse)
async def register_kb(request: KBRegistrationRequest):
    try:
        success, msg = kb_manager.save_kb(
            request.name, 
            request.kb_id, 
            request.ds_id, 
            request.bucket, 
            request.prefix
        )
        if success:
            return ApiResponse(status="success", message=msg)
        else:
            return ApiResponse(status="error", message=msg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/admin/kbs/{kb_id}", response_model=ApiResponse)
async def delete_kb(kb_id: str):
    try:
        success, msg = kb_manager.delete_kb(kb_id)
        if success:
            return ApiResponse(status="success", message=msg)
        else:
            return ApiResponse(status="error", message=msg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/admin/upload-and-sync", response_model=ApiResponse)
async def upload_and_sync(
    kb_id: str = Form(...),
    ds_id: str = Form(...),
    bucket: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        s3 = get_s3_client()
        agent_client = get_bedrock_agent_client()
        
        # 1. S3 업로드
        file_content = await file.read()
        target_key = file.filename
        
        s3.put_object(
            Bucket=bucket,
            Key=target_key,
            Body=file_content,
            ContentType="application/pdf"
        )
        
        # 2. Ingestion Job 시작
        response = agent_client.start_ingestion_job(
            knowledgeBaseId=kb_id, 
            dataSourceId=ds_id
        )
        job_id = response['ingestionJob']['ingestionJobId']
        
        return ApiResponse(
            status="success",
            message="파일 업로드 및 동기화 시작됨",
            data={
                "job_id": job_id,
                "kb_id": kb_id,
                "ds_id": ds_id
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/admin/ingest-status/{kb_id}/{ds_id}/{job_id}", response_model=ApiResponse)
async def check_status(kb_id: str, ds_id: str, job_id: str):
    try:
        client = get_bedrock_agent_client()
        response = client.get_ingestion_job(
            knowledgeBaseId=kb_id, 
            dataSourceId=ds_id, 
            ingestionJobId=job_id
        )
        status = response['ingestionJob']['status']
        return ApiResponse(
            status="success",
            message="상태 조회 성공",
            data={"status": status}
        )
    except Exception as e:
        return ApiResponse(status="error", message=str(e), data={"status": "ERROR"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
