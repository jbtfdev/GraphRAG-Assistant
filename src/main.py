import numpy as np

import os
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

from src.models.embedding_model import model
from src.ingestion.pdf_loader import load_pdf
from src.Chunking.text_chunker import chunk_text
from src.embedding.embedder import embedd
from src.retriever.vector_store import vector_store
from src.llm.generator import generator_answer

path = "data/papers/1412.6980v9.pdf"
load = load_pdf(path)
chunks = chunk_text(load)
embeds = embedd(chunks)
index, stored_chunks = vector_store(embeds)

Q = input("Enter Your Query : ")
Q_vector = model.encode(Q)
Q_vector = np.array([Q_vector], dtype="float32")

D, I = index.search(Q_vector, k=3)
top_chunks = [stored_chunks[i] for i in I[0]]

Response = generator_answer(Q,top_chunks)
print(f"---- answer ----\n")
print(f"->{Response}")