from src.ingestion.pdf_loader import load_pdf


def chunk_text(text):
    text = text.split()
    chunk_size=100
    chunked = []
    for z in range(0,len(text), chunk_size):
        chunk = text[z : z+chunk_size]
        chunk = " ".join(chunk)
        chunked.append(chunk)
    
    return chunked












'''jk = load_pdf("data/papers/1412.6980v9.pdf")
kaki = chunk_text(jk)
print(kaki[0])
print("---------------------")
print(kaki[1])'''