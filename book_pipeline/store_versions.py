from db import store_in_chromadb, get_all_versions

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def check_all_versions():
    results = get_all_versions()

    print(f"Total versions stored: {len(results['documents'])}\n")
    
    for doc, meta in zip(results["documents"], results["metadatas"]):
        print(f"Title: {meta['title']}")
        print(f"Version: {meta['version']}")
        print(f"Timestamp: {meta['timestamp']}")
        print(f"Likes: {meta['likes']} | 👁️ Clicks: {meta['clicks']} | 🧠 Score: {meta['score']:.2f}")
        print(f"Preview: {doc[:100]}...\n")

if __name__ == "__main__":
    original_text = read_file(r"C:\Users\Siddu\Downloads\New folder\Internshala_project\chapter1.txt")
    ai_text       = read_file(r"C:\Users\Siddu\Downloads\New folder\Internshala_project\newtext.txt")
    human_text    = read_file(r"C:\Users\Siddu\Downloads\New folder\Internshala_project\final_text.txt")

    store_in_chromadb(original_text, chapter_title="Chapter 1", version="v1.0 - Original")
    store_in_chromadb(ai_text, chapter_title="Chapter 1", version="v2.0 - AI Rewritten")
    store_in_chromadb(human_text, chapter_title="Chapter 1", version="v3.0 - Human Reviewed")

    print("All versions stored in persistent ChromaDB!\n")
    
    check_all_versions()
