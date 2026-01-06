# Retrieval-Augmented-Generation

Based on https://developers.llamaindex.ai/python/framework/

Hardware: HP OmniBook X Flip 16-as0178ng (16,0" 2.8k OLED Touch, Intel Core Ultra 7 258V (8C), 32GB RAM, 2TB SSD, Windows 11) 


## Technology Stack

- LLM: Choose [Ollama](https://ollama.com/) over LM Studio, because it is fully open-source, supports my hardware setup, and is known for its simplicity.
- PDF Processing: [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/index.html), because it is efficient and supports OCR, office documents (paid version) and LLM frameworks with RAG (like [LlamaIndex](https://github.com/run-llama/llama_index)), optionally with [Unstructured](https://unstructured.io/blog/how-to-process-pdf-in-python). 
- Local embeddings: [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) 
- (Vector database: [Qdrant Vector Store](https://github.com/qdrant/qdrant) - postponed, using simple JSON-based persist for now)  
- RAG framework: [LlamaIndex](https://github.com/run-llama/llama_index) instead of LangChain
- (API Layer: [FastAPI](https://fastapi.tiangolo.com/)?)
