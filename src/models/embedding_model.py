import os
from contextlib import redirect_stdout, redirect_stderr

fnull = open(os.devnull, "w")

with redirect_stdout(fnull), redirect_stderr(fnull):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")