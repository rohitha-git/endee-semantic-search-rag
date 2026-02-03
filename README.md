# Semantic Search and RAG using Endee (Vector Database)

## Project Overview
Traditional keyword-based search systems often fail to understand the semantic meaning of user queries. This project demonstrates how vector databases can be used to build intelligent AI systems that retrieve information based on meaning rather than exact keyword matches.

The project implements:
- Semantic Search
- Retrieval-Augmented Generation (RAG)

The system is designed around Endee, a vector database solution, where vector search is the core component of the application.

---

## Problem Statement
Users frequently need to search large collections of text documents and retrieve relevant information based on intent and meaning. Keyword-based approaches are limited and often return incomplete or irrelevant results.

The objective of this project is to:
- Convert documents into vector embeddings
- Store and retrieve embeddings using vector similarity search
- Use retrieved documents as contextual knowledge to generate better answers

---

## System Design / Technical Approach

### Architecture
User Query  
↓  
Embedding Model (Sentence Transformers)  
↓  
Vector Similarity Search (Endee Concept)  
↓  
Relevant Documents  
↓  
RAG Answer Generation  

---

### Workflow
1. Load textual documents from a dataset  
2. Convert documents into dense vector embeddings  
3. Store embeddings in a vector-based retrieval system  
4. Convert user query into an embedding  
5. Perform cosine similarity search to retrieve relevant documents  
6. Use retrieved documents as context for answer generation (RAG)  

---

## Use of Endee
Endee is designed as a client for an external vector database service that supports index-based vector storage and similarity search.

In this project:
- Endee is used as the conceptual vector database layer  
- The project follows Endee’s intended workflow:
  - Vector embedding  
  - Vector storage  
  - Semantic similarity retrieval  
- For ease of local execution and evaluation, vector storage and similarity search are simulated in-memory while preserving the same retrieval logic used in Endee-based systems  

This approach keeps the project lightweight and runnable locally while clearly demonstrating how Endee is used in AI applications where vector search is central.

---

## Retrieval-Augmented Generation (RAG)

### What is RAG?
Retrieval-Augmented Generation (RAG) combines information retrieval with answer generation. Instead of generating answers only from a model’s internal knowledge, the system retrieves relevant documents and uses them as context.

### RAG Workflow
Query → Vector Search → Relevant Context → Answer Generation  

### Benefits of RAG
- Reduces hallucinations  
- Improves factual accuracy  
- Grounds answers in external knowledge  
- Scales to large document collections  

---

## Technologies Used
- Python 3  
- SentenceTransformers (all-MiniLM-L6-v2)  
- NumPy  
- Scikit-learn  
- Endee (Vector Database – conceptual integration)  

---

## Project Structure
endee-rag-document-qa/
│
├── data/
│ └── sample_docs.txt
│
├── src/
│ ├── embeddings.py
│ ├── query.py
│ ├── rag_pipeline.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

## Setup Instructions

### 1. Clone the Repository
git clone <your-github-repo-link>
cd endee-rag-document-qa


### 2. Create and Activate Virtual Environment
python -m venv venv


---

### 3. Install Dependencies
pip install -r requirements.txt
pip install scikit-learn


---

## Running the Project

### Semantic Search
python -m src.query


### RAG Pipeline
python -m src.rag_pipeline


---

## Example Output

Input: What is NLP?

Retrieved Context:
Natural Language Processing (NLP) allows machines to understand and process human language.
Machine learning is a subset of artificial intelligence that enables systems to learn from data.

Generated Answer: Based on the available documents, Natural Language Processing (NLP) allows machines to understand and process human language.


---

## Use Cases
- Semantic Search  
- Question Answering Systems  
- Retrieval-Augmented Generation (RAG)  
- Recommendation Systems  
- Knowledge Retrieval Applications  

---

## Conclusion
This project demonstrates how vector databases like Endee can be used to build intelligent AI systems where vector search is the core component. By combining semantic search with RAG, the system retrieves relevant information and generates accurate, context-aware answers.

---

## Author
N.Rohitha
Project – Endee Vector Database


