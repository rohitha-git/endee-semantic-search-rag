import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def retrieve_documents(query, documents, doc_embeddings, top_k=3):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    top_indices = similarities.argsort()[-top_k:][::-1]
    return [documents[i] for i in top_indices]

def generate_answer(query, context_docs):
    context = " ".join(context_docs)

    answer = f"""
Question:
{query}

Answer:
Based on the available documents, {context}
"""
    return answer.strip()

if __name__ == "__main__":
    print(" RAG Pipeline Started\n")

    documents = load_documents("data/sample_docs.txt")
    doc_embeddings = model.encode(documents)

    print("\nType your question below and press Enter")
    query = input(">>> ")


    retrieved_docs = retrieve_documents(query, documents, doc_embeddings)

    final_answer = generate_answer(query, retrieved_docs)

    print("\n Retrieved Context:\n")
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"{i}. {doc}")

    print("\n Final Answer:\n")
    print(final_answer)
