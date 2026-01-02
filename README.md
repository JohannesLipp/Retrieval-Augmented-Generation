# Retrieval-Augmented-Generation

Based on https://developers.llamaindex.ai/python/examples/low_level/oss_ingestion_retrieval/

Hardware: HP OmniBook X Flip 16-as0178ng (16,0" 2.8k OLED Touch, Intel Core Ultra 7 258V (8C), 32GB RAM, 2TB SSD, Windows 11) 

## Organize everything in services, even locally:

1) PDFs
2) Document Loader
3) Text Chunking
4) Embedding Model (local)
5) Vector Database (local)
6) Retriever
7) LLM (local)
8) API (FastAPI)
9) UI (optional)

## Technology Stack

- LLM: Choose [Ollama](https://ollama.com/) over LM Studio, because it is fully open-source, supports my hardware setup, and is known for its simplicity.
- PDF Processing: [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/index.html), because it is efficient and supports OCR, office documents (paid version) and LLM frameworks with RAG (like [LlamaIndex](https://github.com/run-llama/llama_index)), optionally with [Unstructured](https://unstructured.io/blog/how-to-process-pdf-in-python). 
- Local embeddings: [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) or Qdrant FastEmbed Embeddings 
- Vector database: [Qdrant Vector Store](https://github.com/qdrant/qdrant), because it allows many applications and it kubernetes-native.  
- RAG framework: [LlamaIndex](https://github.com/run-llama/llama_index) instead of LangChain
- API Layer: [FastAPI](https://fastapi.tiangolo.com/)?

## Step-by-step Instructions
- Download Docker and enable Kubernetes support
  - Verify via `docker --version` and `kubectl cluster-info`
- Download [Helm](https://github.com/helm/helm/releases)  
  - Verify via `helm version`
- Run Qdrant vector store
  - `helm repo add qdrant https://qdrant.to/helm`
  - `helm install qdrant qdrant/qdrant`
  - Verify 
    - In a new terminal expose port `kubectl port-forward service/qdrant 6333:6333`
    - `kubectl get pods`
    - `curl localhost:6333`
- Continue in the [RAG Jupyter Notebook](RAG.ipynb)
