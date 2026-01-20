import numpy as np 
import faiss
import pandas as pd 
from sentence_transformers import SentenceTransformer

model =SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("embeddings/faiss_index.bin")
df = pd.read_csv("data/issues.csv")

def search(query, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    
    print("\n Similar cases: \n")
    for i in indices[0]:
        row = df.iloc[i]
        print(f"-{row['issue']}")
        print(f" Solution: {row['solution']}\n")
        
if __name__ == "__main__":
    query = input("Describe the issue: ")
    search(query)