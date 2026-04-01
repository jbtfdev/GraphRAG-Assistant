# GraphRAG v0.5 — Explainable Hybrid Retrieval System

GraphRAG v0.5 is a hybrid retrieval system that combines **knowledge graphs (Neo4j)** with **vector search (FAISS)** and **LLMs** to generate more grounded and explainable answers.

Instead of relying only on semantic similarity, this system introduces **entity-aware retrieval and structured relationships** into the RAG pipeline.

---

## 🚀 Features

- Hybrid Retrieval (Graph + Vector)
- Entity Extraction from Queries
- Knowledge Graph Integration (Neo4j)
- Semantic Search using FAISS
- LLM-based Answer Generation
- Modular Pipeline (Ingestion → Retrieval → Generation)

---

## 🧠 How It Works
User Query
↓
Entity Extraction
↓
Graph Retrieval (Neo4j)
↓
Vector Retrieval (FAISS)
↓
Combine Context
↓
LLM Response


---

## ⚙️ System Components

### 1. Ingestion Pipeline
- Processes text / documents
- Extracts:
  - Entities
  - Relationships
- Stores:
  - Graph data in Neo4j
  - Embeddings in FAISS

---

### 2. Graph Layer (Neo4j)
- Nodes: Entities (e.g., Metformin, Type 2 Diabetes)
- Relationships: (e.g., TREATS, ASSOCIATED_WITH)
- Enables structured reasoning and connections

---

### 3. Vector Store (FAISS)
- Stores embeddings of chunks
- Enables semantic similarity search

---

### 4. Retrieval Layer
- Extracts entities from user query
- Fetches:
  - Graph-based context
  - FAISS-based context
- Combines both for richer understanding

---

### 5. Generation Layer (LLM)
- Takes combined context
- Produces grounded and informative answers

---

## 🧪 Example Query
What treats Type 2 diabetes and how does it work?

**System Behavior:**
- Extracts entity: "Type 2 diabetes"
- Graph retrieval finds: "Metformin → TREATS → Type 2 diabetes"
- FAISS provides supporting context
- LLM generates a structured answer

---

## 📦 Tech Stack

- Python
- Neo4j (Graph Database)
- FAISS (Vector Search)
- Sentence Transformers (Embeddings)
- LLM (Local / API-based)
- PyTorch

---

## ⚡ Current Status — v0.5

This version includes:
- Core GraphRAG pipeline
- Hybrid retrieval (Graph + Vector)
- Entity-based reasoning
- Working CLI-based interaction

---

## 🔜 Next Steps

- FastAPI integration for serving queries
- UI for interactive querying
- Improved relation extraction accuracy
- Context ranking and filtering
- Expanded domain-specific datasets

---

## 🧠 Key Insight

Traditional RAG:
> Query → Vector Search → Answer

GraphRAG:
> Query → Entities → Graph + Vector → Answer

This enables more **connected, explainable, and context-aware responses**.

---

## 📌 Note

This is an evolving project aimed at exploring **structured retrieval + LLM integration** for more reliable AI systems.

---

## 👤 Author

Built as part of a focused effort to develop **practical ML/AI systems with real-world relevance**.

---


