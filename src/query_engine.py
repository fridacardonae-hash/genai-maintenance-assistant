import faiss
import numpy as np 
import pandas as pd 
from sentence_transformers import SentenceTransformer
from src.llm_client import ask_llm
import os

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"


model = SentenceTransformer("models/all-MiniLM-L6-v2", device="cpu")
#model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("embeddings/faiss_index.bin")
df = pd.read_csv("data/issues.csv")

def ask_question(question, k=3):
    #convertit a embedding la pregunta
    question_embedding = model.encode([question])
    
    #faiss index mide vectores para buscar similares entre el indice embedding(index) y la pregunta hecha embedding
    distances, indices = index.search(
        np.array(question_embedding), k
    )
    
    #construir texto
    context = ""
    for idx in indices[0]:
        row = df.iloc[idx]
        context += f"""
Issue: {row["issue"]}
Solution: {row["solution"]}
---
"""
    prompt = f"""
You are an industrial maintenance assistant. 
Use only the following past issues and solutions to answer the question. 

Context: 
{context}

Question:
{question}

Answer clearly and step by step. 
"""
    return ask_llm(prompt)
