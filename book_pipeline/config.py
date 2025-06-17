import os

# Always resolve the same absolute path for ChromaDB storage
CHROMA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "chromadb_store"))
