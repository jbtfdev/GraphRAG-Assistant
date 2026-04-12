import os
import numpy as np
import faiss
import pickle
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

# path = "data/papers/1412.6980v9.pdf"
# load = load_pdf(path)
# chunks = chunk_text(load)
# embeds = embedd(chunks)
# pdf_index, stored_chunks = vector_store(embeds)

#PUBMED FAISS
p_index = faiss.read_index("data/vector/pubmed_index.faiss")
with open("data/vector/pubmed_metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

#QUERY INPUT+ENTITY RETRAC
Q = input("Enter Your Query : ")
Q_vector = model.encode(Q)
Q_vector = np.array([Q_vector], dtype="float32")
Q_entity = extract_entities(Q)

#PUBMED RAG
X, pm_I = p_index.search(Q_vector, k=7)
results = [metadata[i] for i in pm_I[0]]
result_texts = [result["text"] for result in results]


#PDF RAG
# D, I = pdf_index.search(Q_vector, k=3)
# top_chunks = [stored_chunks[i] for i in I[0]]

#GRAPH RETRIEVAL 
graph_chunks = []
for e in Q_entity:
    name = e["entity"].lower().strip()
    chunks = graph_ret.get_graph_chunks(name)
    graph_chunks.extend(chunks)

# f_chunks = graph_chunks + top_chunks
context = graph_chunks + result_texts


Response = generator_answer(Q,context)
print(f"---- answer ----\n")
print(f"->{Response}")