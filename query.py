import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

if __name__ == "__main__":
    print(" Semantic Search Demo (Easy Mode)")
    print("Loading documents...\n")

    documents = load_documents("data/sample_docs.txt")
    doc_embeddings = model.encode(documents)

    print("Documents loaded successfully!")
    query = input("\n>>> Enter your question: ")

    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    top_k = 3
    top_indices = similarities.argsort()[-top_k:][::-1]

    print("\nTop Relevant Results:\n")
    for i, idx in enumerate(top_indices, 1):
        print(f"{i}. {documents[idx]}")
