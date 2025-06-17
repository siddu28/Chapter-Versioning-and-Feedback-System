from config import CHROMA_PATH
import chromadb
from datetime import datetime
import uuid

def store_in_chromadb(text, chapter_title="Chapter 1", version="v1.0"):
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(name="book_versions")

    metadata = {
        "title": chapter_title,
        "version": version,
        "timestamp": datetime.now().isoformat(),
        "likes": 0,
        "clicks": 0,
        "score": 0.0
    }

    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[str(uuid.uuid4())]
    )

def get_all_versions():
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(name="book_versions")
    
    results = collection.get(include=["documents", "metadatas"])
    
    # Add back IDs separately (workaround)
    ids = collection.peek()["ids"]
    results["ids"] = ids
    return results
