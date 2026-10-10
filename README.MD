RAG & MCP Lab

Personal experiments with Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), vector databases, and the Model Context Protocol (MCP).

This repository is my personal playground for exploring how LLM-powered applications can retrieve external knowledge, generate context-aware responses, and interact with external tools and data sources.

The goal is to learn by building, testing different approaches, and understanding the components behind modern AI applications.

🔬 Areas of Exploration

- Retrieval-Augmented Generation (RAG) — retrieving relevant information from external knowledge sources to improve LLM responses.
- Local LLMs — experimenting with language models running locally through Ollama.
- Vector Databases — storing embeddings and retrieving semantically relevant documents with ChromaDB.
- Embeddings & Semantic Search — exploring vector representations and similarity-based retrieval.
- Model Context Protocol (MCP) — exploring standardized ways to expose tools and contextual data to AI applications.
- LLM Integration — combining retrieval pipelines and language models to build context-aware applications.

🧪 Current Experiments

Basic RAG Pipeline

The initial experiment implements a minimal RAG workflow using Python, Ollama, and ChromaDB.

Technologies:

- "Ollama" (https://ollama.com/) — local model execution and embeddings.
- "ChromaDB" (https://www.trychroma.com/) — persistent vector storage and similarity search.
- "bge-m3" — embedding model used to represent documents and queries.
- "qwen3.6" — language model configured for response generation.

Workflow:

1. Define a collection of sample documents.
2. Generate document embeddings.
3. Store the documents and embeddings in ChromaDB.
4. Convert a user query into an embedding.
5. Retrieve the most relevant documents using vector similarity.
6. Provide the retrieved context to an LLM.
7. Generate a response grounded in the retrieved information.

The current implementation uses a small set of example documents to demonstrate the fundamental concepts behind RAG.

🏗️ Project Structure

RAG-llama/
├── rag_locale.py   # Initial local RAG experiment
├── .gitignore
└── README.md

The repository is intentionally lightweight and will evolve as new experiments are added.

🚀 Getting Started

Prerequisites

- Python 3.10+
- "Ollama" (https://ollama.com/) installed and running
- The embedding and generation models used by the script

Installation

Clone the repository:

git clone https://github.com/AlbertoPravisano/RAG-llama.git
cd RAG-llama

Install the Python dependencies:

python -m pip install chromadb ollama

Pull the models configured in "rag_locale.py":

ollama pull bge-m3
ollama pull qwen3.6

«Model availability depends on the Ollama registry. If a configured model name is unavailable, choose a compatible model and update the corresponding constant in the script.»

Run the experiment

python rag_locale.py

The script indexes the sample documents, retrieves relevant content for a predefined query, and prints the generated response.

🗺️ Roadmap

- [x] Implement a minimal local RAG pipeline.
- [x] Store and retrieve document embeddings using ChromaDB.
- [ ] Experiment with external document ingestion and chunking.
- [ ] Compare embedding models and retrieval strategies.
- [ ] Explore retrieval quality and response evaluation.
- [ ] Experiment with MCP servers and tool integration.
- [ ] Combine RAG pipelines with MCP-enabled AI applications.
- [ ] Add more self-contained experiments and examples.

This roadmap reflects areas of exploration rather than a commitment to a production-ready implementation.

🎯 Project Philosophy

This is a learning-oriented repository, not a production-ready framework.

Experiments may be incomplete, implementations may change, and examples are intended to make individual concepts easier to understand and test.

The focus is on practical experimentation, understanding architectural choices, and exploring the building blocks of LLM-powered applications.

📄 License

No license has been specified yet. Until a license is added, reuse and redistribution are subject to the default copyright rules.