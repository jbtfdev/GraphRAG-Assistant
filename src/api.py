from fastapi import FastAPI
from pydantic import BaseModel

from src.main import pipeline

app = FastAPI(tittle="MedGraphRAG API")

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
    answer = pipeline(request.query)

    return {
        "query": request.query,
        "answer": answer
    }