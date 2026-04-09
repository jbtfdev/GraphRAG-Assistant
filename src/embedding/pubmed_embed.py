import faiss
import pickle
import json
import numpy as np

from src.embedding.embedder import embedd
from src.retriever.vector_store import vector_store

with open("data/processed/pubmed_chunks.json", "r") as f:
    chunks = json.load(f)
    

texts = [chunk["text"] for chunk in chunks]
pm_embeddings = embedd(texts)
index, vectors = vector_store(pm_embeddings)
faiss.write_index(index, "data/vector/pubmed_index.faiss")
with open("data/vector/pubmed_metadata.pkl", "wb") as f:
    pickle.dump(chunks, f)

