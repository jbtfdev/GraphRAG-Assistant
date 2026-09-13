from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.main import pipeline

app = FastAPI(title="MedGraphRAG API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://medgraph-research-assistant.vercel.app",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health_check():
    return{
        "status" : "ok",
        "message" : "MedGraphRAG API is running"
    }

@app.post("/query")
def query_medgraphrag(request: QueryRequest):
    result = pipeline(request.query)

    return {
        "answer": result["answer"],
        "confidence": 0.0,
        "sources": result["sources"],
        "path": result["path"]
    }

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)