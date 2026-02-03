from endee import Endee
from src.embeddings import generate_embeddings

def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return [line.strip() for line in text.split("\n") if line.strip()]

def ingest():
    docs = load_documents("data/sample_docs.txt")
    vectors = generate_embeddings(docs)

    client = Endee()

    # create index (only once)
    index = client.create_index(
        name="documents",
        dimension=len(vectors[0])
    )

    index.add_vectors(
        ids=[str(i) for i in range(len(docs))],
        vectors=vectors,
        metadata=[{"text": d} for d in docs]
    )

    print(" Documents indexed successfully using Endee")

if __name__ == "__main__":
    ingest()
