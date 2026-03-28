

def chunk_text(text):
    text = text.split()
    chunk_size=300
    chunked = []
    for z in range(0,len(text), chunk_size):
        chunk = text[z : z+chunk_size]
        chunk = " ".join(chunk)
        chunked.append(chunk)
    
    return chunked

