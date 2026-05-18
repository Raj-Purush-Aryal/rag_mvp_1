import os
from dotenv import load_dotenv

import chromadb
from google import genai

from utils.embeddings import get_embedding

# Load environment variables
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Vector DB connection
chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_collection("documents")


# RAG FUNCTION

def ask_question(question):
    print("\nUser question:", question)

    # 1. Convert question to embedding
    question_embedding = get_embedding(question)

    # 2. Retrieve similar chunks from vector DB
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]

    print("\nRetrieved chunks:")
    for chunk in retrieved_chunks:
        print("-", chunk)

    # 3. Build context
    context = "\n".join(retrieved_chunks)

    # 4. Prompt for Gemini
    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    # 5. Call Gemini API
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text



# TEST RUN
if __name__ == "__main__":
    answer = ask_question("What is RAG?")
    print("\nFINAL ANSWER:\n")
    print(answer)