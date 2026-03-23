import numpy as np
import faiss 
 

def vector_store(encoded):
    vectors=[]
    chunks=[]
    for text,vector in encoded:
        vectors.append(vector)
        chunks.append(text)

    vectors = np.array(vectors, dtype='float32')
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)
    return index, chunks
