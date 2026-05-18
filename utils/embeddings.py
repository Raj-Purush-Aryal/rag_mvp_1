from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):

    embedding = model.encode(text)

    return embedding.tolist()


sample_text = "RAG combines retrieval with generation."

vector = get_embedding(sample_text)

print("Embedding length:")
print(len(vector))

print("\nFirst 5 values:")
print(vector[:5])