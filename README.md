# 📚 Chapter Versioning and Feedback System
This is a Streamlit-based AI-powered application for generating, editing, storing, and comparing multiple versions of a book chapter. The system supports AI-assisted rewrites, human feedback incorporation, version tracking, and reward scoring via likes/clicks.

🧩 Problem Statement
Book editing often involves multiple revisions by different stakeholders. Managing these versions manually can be error-prone and inefficient.

## Objective:
- Build a system that allows:
- AI-generated rewrites of chapter content.
- Human feedback-driven editing.
- Storage of all versions with searchable metadata.
- Feedback scoring through likes and clicks.

```
book_pipeline/
├── app.py                         # Streamlit UI
├── chapter1.txt                   # Original chapter file
├── db.py                          # Vector DB operations (ChromaDB)
├── writer.py                      # AI rewrite logic
├── editing_with_feedback.py       # Feedback-based editing logic
├── feedback.py                    # Like/Click feedback updater
├── editor_feedback.txt            # Temporary feedback storage

```


🔁 Project Flow (Internal Process)
### Chapter Ingestion
- chapter1.txt is read as the original input.

### AI Rewrite
- writer.py uses an LLM to rewrite the chapter.
- The rewritten version is saved in ChromaDB with metadata like: version (user-defined or default) timestamp, likes, clicks, score, etc.

### Feedback-Based Editing
- User provides feedback via UI.
- editing_with_feedback.py takes the original text + feedback and sends it to the LLM.
- The result is stored in ChromaDB with a new version tag.

### ChromaDB Integration
- Acts as a local vector store using sentence embeddings.
- All versions are stored with their embeddings + metadata.

### Version Browsing and Filtering
- get_all_versions() fetches all entries.
- Sorted by a custom score = 0.6 * likes + 0.4 * clicks.
- Users can filter by minimum score via a slider.

### Feedback Update
- Likes and clicks are updated in metadata using update_feedback().
- Score is recalculated dynamically.


### Streamlit UI
![Image](https://github.com/user-attachments/assets/1c176f3b-cec2-43b1-9f8d-2288e47a4eb9)

![Image](https://github.com/user-attachments/assets/0936e18a-842c-42d1-8227-204f1a14d099)




## Setup Instructions

1. **Clone the repository**:
   ```bash
   https://github.com/siddu28/Chapter-Versioning-and-Feedback-System

   
3. **Run the streamlit app:**:   
   ```commandline
    streamlit run streamlit_app.py
   ```
