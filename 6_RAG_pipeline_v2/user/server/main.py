import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import boto3
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI(
    title="RAG User API",
    description="사용자용 질의응답 API",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str
    session_id: str

class Source(BaseModel):
    content: str
    page: int
    document_title: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    sources: List[Source]

class ApiResponse(BaseModel):
    status: str
    message: str
    data: Optional[dict] = None

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "User API is running"}

@app.get("/api/documents", response_model=ApiResponse)
async def get_documents():
    try:
        conn = get_db_connection()
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT 
                metadata->>'filename' as filename,
                metadata->>'document_file_id' as document_file_id,
                COUNT(*) as chunk_count,
                MAX(created_at) as latest_created_at
            FROM documents
            GROUP BY metadata->>'filename', metadata->>'document_file_id'
            ORDER BY MAX(created_at) DESC
        """)
        rows = cursor.fetchall()
        documents = []
        for r in rows:
            try:
                doc_id = int(r[1]) if r[1] and str(r[1]).strip() else None
            except (ValueError, TypeError):
                doc_id = None
            documents.append({
                "id": doc_id,
                "title": r[0] or "Untitled",
                "chunk_count": r[2],
                "created_at": r[3].isoformat() if r[3] else None
            })
        cursor.close()
        conn.close()
        return ApiResponse(status="success", message="Documents retrieved", data={"documents": documents})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        from langchain_aws import ChatBedrock, BedrockEmbeddings
        from langchain_core.messages import HumanMessage
        
        bedrock_client = boto3.client("bedrock-runtime", region_name=os.getenv('AWS_REGION', 'us-east-1'))
        embeddings = BedrockEmbeddings(client=bedrock_client, model_id="amazon.titan-embed-text-v1")
        query_embedding = embeddings.embed_query(request.query)
        embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT content, metadata FROM documents
            ORDER BY embedding <=> %s::vector LIMIT 3
        """, (embedding_str,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        context_text = "\n".join([r[0] or "" for r in results])
        sources = []
        for r in results:
            content, metadata = r
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
                content=(content or "")[:200],
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
        prompt = f"문서 내용:\n{context_text}\n\n질문: {request.query}\n\n답변:"
        response = llm.invoke([HumanMessage(content=prompt)])
        response_text = response.content if isinstance(response.content, str) else str(response.content)
        
        return ChatResponse(response=response_text, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/chat-history/{session_id}")
async def clear_history(session_id: str):
    return {"status": "success"}

# Mount client build directory if it exists
build_dir = os.path.join(os.path.dirname(__file__), "../client/build")
if os.path.exists(build_dir):
    app.mount("/", StaticFiles(directory=build_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
