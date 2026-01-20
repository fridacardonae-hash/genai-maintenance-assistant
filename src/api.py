from fastapi import FastAPI
from pydantic import BaseModel
from src.query_engine import ask_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "Industrial RAG Assistant",
    description = "GenAI assistant for machine troubleshooting",
    version = "1.0.0"
    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
class QuestionRequest(BaseModel):
    question: str
    
class AnswerResponse(BaseModel):
    answer: str
    
@app.post("/ask", response_model=AnswerResponse)
def ask_rag(request: QuestionRequest):
    answer = ask_question(request.question)
    return {"answer": answer}