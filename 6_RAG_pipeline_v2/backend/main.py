import os
import json
import os
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import boto3
import psycopg2
from dotenv import load_dotenv
import uuid

load_dotenv()

app = FastAPI(
    title="RAG Chatbot API",
    description="문서 기반 질의응답 시스템 API",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Document(BaseModel):
    id: int
    title: str
    category: str
    description: Optional[str] = None
    queryable_topics: List[str]
    example_questions: List[str]
    uploaded_at: Optional[str] = None


class ChatRequest(BaseModel):
    query: str
    session_id: str


class Source(BaseModel):
    content: str
    page: int
    document_id: Optional[int] = None
    document_title: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    sources: List[Source]


class ApiResponse(BaseModel):
    status: str
    message: str
    data: Optional[dict] = None


def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    conn.autocommit = True
    return conn


def get_s3_client():
    return boto3.client('s3', region_name=os.getenv('AWS_REGION', 'us-east-1'))


@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "RAG Chatbot API is running"}


@app.get("/api/documents", response_model=ApiResponse)
async def get_documents():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT DISTINCT 
                metadata->>'filename' as filename,
                metadata->>'s3_key' as s3_key,
                metadata->>'document_file_id' as document_file_id,
                COUNT(*) as chunk_count,
                MAX(created_at) as latest_created_at
            FROM documents
            WHERE metadata->>'filename' IS NOT NULL
            GROUP BY metadata->>'filename', metadata->>'s3_key', metadata->>'document_file_id'
            ORDER BY MAX(created_at) DESC
        """)
        
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        
        documents = []
        for row in rows:
            filename, s3_key, document_file_id, chunk_count, created_at = row
            try:
                doc_id = int(document_file_id) if document_file_id and str(document_file_id).strip() else None
            except (ValueError, TypeError):
                doc_id = None
            doc = {
                "id": doc_id,
                "title": filename or "Untitled",
                "s3_key": s3_key,
                "chunk_count": chunk_count,
                "created_at": created_at.isoformat() if created_at else None
            }
            documents.append(doc)
        
        return ApiResponse(
            status="success",
            message="Documents retrieved successfully",
            data={"documents": documents}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        from langchain_aws import ChatBedrock, BedrockEmbeddings
        from langchain_core.messages import HumanMessage
        
        bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
        
        embeddings = BedrockEmbeddings(
            client=bedrock_client,
            model_id="amazon.titan-embed-text-v1"
        )
        
        query_embedding = embeddings.embed_query(request.query)
        embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT content, metadata,
                   1 - (embedding <=> %s::vector) as similarity
            FROM documents
            ORDER BY embedding <=> %s::vector
            LIMIT 3
        """, (embedding_str, embedding_str))
        
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        sources = []
        context_text = ""
        for content, metadata, similarity in results:
            context_text += f"\n{content}\n"
            if metadata:
                try:
                    meta_dict = json.loads(metadata) if isinstance(metadata, str) else metadata
                    page = meta_dict.get("page", 0)
                    doc_title = meta_dict.get("filename", meta_dict.get("title", "Unknown"))
                except (json.JSONDecodeError, AttributeError, TypeError):
                    page = 0
                    doc_title = "Unknown"
            else:
                page = 0
                doc_title = "Unknown"
            sources.append(Source(
                content=content[:200] if content else "",
                page=page,
                document_title=doc_title
            ))
        
        llm = ChatBedrock(
            client=bedrock_client,
            model_id="anthropic.claude-3-haiku-20240307-v1:0",
            model_kwargs={
                "max_tokens": 2000,
                "temperature": 0.1
            }
        )
        
        prompt = f"""다음 문서를 참고하여 질문에 답해주세요.

문서 내용:
{context_text}

질문: {request.query}

답변:"""
        
        message = HumanMessage(content=prompt)
        response = llm.invoke([message])
        
        response_text = response.content if isinstance(response.content, str) else str(response.content)
        
        return ChatResponse(
            response=response_text,
            sources=sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/chat-history/{session_id}", response_model=ApiResponse)
async def clear_chat_history(session_id: str):
    try:
        return ApiResponse(
            status="success",
            message="Chat history cleared successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/admin/documents", response_model=ApiResponse)
async def get_admin_documents():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT DISTINCT 
                metadata->>'filename' as filename,
                metadata->>'s3_key' as s3_key,
                metadata->>'document_file_id' as document_file_id,
                COUNT(*) as chunk_count,
                MAX(created_at) as latest_created_at
            FROM documents
            WHERE metadata->>'filename' IS NOT NULL
            GROUP BY metadata->>'filename', metadata->>'s3_key', metadata->>'document_file_id'
            ORDER BY MAX(created_at) DESC
        """)
        
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        
        documents = []
        for row in rows:
            filename, s3_key, document_file_id, chunk_count, created_at = row
            doc = {
                "id": int(document_file_id) if document_file_id else None,
                "title": filename,
                "s3_key": s3_key,
                "chunk_count": chunk_count,
                "created_at": created_at.isoformat() if created_at else None
            }
            documents.append(doc)
        
        return ApiResponse(
            status="success",
            message="Admin documents retrieved successfully",
            data={"documents": documents}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/admin/documents", response_model=ApiResponse)
async def upload_document(
    file: UploadFile = File(...)
):
    try:
        s3_client = get_s3_client()
        bucket_name = os.getenv('BUCKET_NAME')
        
        if not bucket_name:
            raise ValueError("BUCKET_NAME environment variable is not set")
        
        file_content = await file.read()
        file_key = f"documents/{uuid.uuid4()}_{file.filename}"
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_key,
            Body=file_content,
            ContentType="application/pdf"
        )
        
        return ApiResponse(
            status="success",
            message="Document uploaded to S3 successfully",
            data={"s3_key": file_key, "bucket": bucket_name}
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/admin/documents/{doc_id}", response_model=ApiResponse)
async def delete_document(doc_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            DELETE FROM documents 
            WHERE metadata->>'document_file_id' = %s
        """, (str(doc_id),))
        
        deleted_count = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        
        return ApiResponse(
            status="success",
            message=f"Document and {deleted_count} chunks deleted successfully",
            data={"deleted_chunks": deleted_count}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/api/admin/documents/{doc_id}", response_model=ApiResponse)
async def update_document(doc_id: int, guidelines: dict):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT metadata FROM documents WHERE id = %s", (doc_id,))
        row = cursor.fetchone()
        
        if not row:
            raise HTTPException(status_code=404, detail="Document not found")
        
        metadata = row[0] or {}
        metadata.update({
            "queryable_topics": guidelines.get("queryable_topics", []),
            "example_questions": guidelines.get("example_questions", [])
        })
        
        cursor.execute(
            "UPDATE documents SET metadata = %s WHERE id = %s",
            (json.dumps(metadata), doc_id)
        )
        
        cursor.close()
        conn.close()
        
        return ApiResponse(
            status="success",
            message="Document guidelines updated successfully",
            data={"document": metadata}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
