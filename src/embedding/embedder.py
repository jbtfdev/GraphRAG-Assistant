from src.ingestion.pdf_loader import load_pdf
from src.Chunking.text_chunker import chunk_text
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
def embedd(chunks):
    embeddings = model.encode(chunks)
    encoded = list(zip(chunks,embeddings))
    
    return encoded




'''jk = load_pdf("data/papers/1412.6980v9.pdf")
kaki = chunk_text(jk)
batman = embedd(kaki)
print(batman[10])'''