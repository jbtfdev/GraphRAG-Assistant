import numpy as np
import os
from dotenv import load_dotenv
from src.models.embedding_model import model
from src.ingestion.pdf_loader import load_pdf
from src.Chunking.text_chunker import chunk_text
from src.embedding.embedder import embedd
from src.retriever.vector_store import vector_store
from src.llm.generator import generator_answer
from src.graph.entity import extract_entities
from src.graph.retriever import GraphRetriever


load_dotenv()
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

graph_ret = GraphRetriever(uri,user,password)

path = "data/papers/1412.6980v9.pdf"
load = load_pdf(path)
chunks = chunk_text(load)
embeds = embedd(chunks)
index, stored_chunks = vector_store(embeds)

Q = input("Enter Your Query : ")
Q_vector = model.encode(Q)
Q_vector = np.array([Q_vector], dtype="float32")
Q_entity = extract_entities(Q)

D, I = index.search(Q_vector, k=3)
top_chunks = [stored_chunks[i] for i in I[0]]
graph_chunks = []

for e in Q_entity:
    name = e["entity"].lower().strip()
    chunks = graph_ret.get_graph_chunks(name)
    graph_chunks.extend(chunks)

f_chunks = graph_chunks + top_chunks


Response = generator_answer(Q,graph_chunks)
print(f"---- answer ----\n")
print(f"->{Response}")