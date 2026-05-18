import chromadb
from utils.embeddings import get_embedding

client = chromadb.PersistentClient(path="db")
collection = client.get_or_create_collection("documents")


text = """
RAG stands for Retrieval Augmented Generation.
It combines search systems with large language models.
It is very useful for question answering and summarization tasks.
"""
def chunk_text(text, size=50):
    return [text[i:i+size] for i in range(0, len(text), size)]

chunks = chunk_text(text)
print(chunks)

for i, chunk in enumerate(chunks):

    embedding = get_embedding(chunk)

    collection.add(
        ids=[f"doc_{i}"],
        documents=[chunk],
        embeddings=[embedding]
    )

print("Data stored in vector DB")
results = collection.get()
print(results)
