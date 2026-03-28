from src.models.embedding_model import model

def embedd(chunks):
    embeddings = model.encode(chunks)
    encoded = list(zip(chunks,embeddings))
    
    return encoded



