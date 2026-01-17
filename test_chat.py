from src.query_engine import ask_question

question = input("Whats your question")
answer = ask_question(question)

print(answer)