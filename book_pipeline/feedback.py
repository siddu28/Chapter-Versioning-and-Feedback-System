from config import CHROMA_PATH
import chromadb

def update_feedback(doc_id, like=False, click=False):
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(name="book_versions")

    results = collection.get(ids=[doc_id], include=["metadatas", "documents"])
    if not results["metadatas"]:
        print("Document not found.")
        return

    metadata = results["metadatas"][0]
    likes = metadata.get("likes", 0) + (1 if like else 0)
    clicks = metadata.get("clicks", 0) + (1 if click else 0)
    score = likes / clicks if clicks > 0 else 0.0

    metadata.update({
        "likes": likes,
        "clicks": clicks,
        "score": score
    })

    collection.update(ids=[doc_id], metadatas=[metadata])
