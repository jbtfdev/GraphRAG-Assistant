from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.main import pipeline

app = FastAPI(title="MedGraphRAG API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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
    answer = pipeline(request.query)

    return {
        "answer": answer,
        "confidence" : 0.0,
        "sources" : [],
        "path" : []
    }