## Architecture

```mermaid
graph TD
A[User Question] --> B[FastAPI Endpoint /ask]
B --> C[SentenceTransformers Embedding]
C --> D[FAISS Vector Search]
D --> E[Relevant Context]
E --> F[LLM - Ollama]
F --> G[Generated Answer]
