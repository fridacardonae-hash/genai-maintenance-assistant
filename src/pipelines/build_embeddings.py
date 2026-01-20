import pandas as pd 
import faiss
import numpy as np 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
df = pd.read_csv("data/issues.csv")

texts = []
for _, row, in df.iterrows():
    text = f"""
    Line: {row['line']}
    Machine: {row['machine']}
    Error: {row['error']}
    Issue: {row['issue']}
    Solution: {row['solution']}
    """
    texts.append(text.strip())

embeddings = model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, "embeddings/faiss_index.bin")

print("Embeddings creados")