# app.py (Streamlit App)
import streamlit as st
from db import get_all_versions, store_in_chromadb
from feedback import update_feedback
from writer import spin_chapter
from editing_with_feedback import apply_feedback

st.set_page_config(page_title="📚 Chapter Version Viewer", layout="centered")
st.title("📚 Chapter Version Viewer with Feedback")

CHAPTER_FILE_PATH = "chapter1.txt"
FEEDBACK_FILE = "editor_feedback.txt"

# Version name input
st.markdown("### Version Naming")
version_name = st.text_input("Enter a version name (e.g., v2.1 - Improved Flow):")

st.markdown("### Load and Rewrite Chapter")

# Read original chapter text
try:
    with open(CHAPTER_FILE_PATH, "r", encoding="utf-8") as f:
        original_text = f.read()
except FileNotFoundError:
    st.error(f"Chapter file not found at {CHAPTER_FILE_PATH}")
    st.stop()

# Allow user to trigger AI rewrite
if st.button("Rewrite with AI"):
    if not version_name.strip():
        st.warning("Please enter a version name before rewriting.")
    else:
        ai_text = spin_chapter(original_text)
        store_in_chromadb(ai_text, chapter_title="Chapter 1", version=version_name)
        st.success(f"AI version '{version_name}' stored!")
        st.rerun()

# Allow user to provide feedback and edit
st.markdown("### Feedback-Based Editing")
feedback = st.text_area("Enter your feedback for improvement")

if st.button("🖋️ Generate Edited Version"):
    if not feedback.strip():
        st.warning("Please enter feedback text first.")
    elif not version_name.strip():
        st.warning("Please enter a version name before editing.")
    else:
        with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
            f.write(feedback)

        edited_text = apply_feedback(original_text, feedback)
        store_in_chromadb(edited_text, chapter_title="Chapter 1", version=version_name)
        st.success(f"Human-edited version '{version_name}' stored!")
        st.rerun()


# Browse stored versions
st.divider()
st.markdown("### Browse Stored Versions")
results = get_all_versions()


# Combine and sort
combined = list(zip(results["documents"], results["metadatas"], results.get("ids", [])))
combined.sort(key=lambda x: x[1].get("score", 0.0), reverse=True)



# Filter by minimum score
min_score = st.slider("🎯 Minimum Score Filter", 0.0, 1.0, 0.0, 0.1)
filtered = [entry for entry in combined if entry[1].get("score", 0.0) >= min_score]

if not filtered:
    st.warning("No versions found with this score filter.")
else:
    for idx, (doc, meta, doc_id) in enumerate(filtered):
        with st.expander(f"📘 {meta['title']} — {meta['version']}", expanded=False):
            st.markdown(f"📝 **Preview:**\n\n{doc}")

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"Like", key=f"like-{idx}"):
                    update_feedback(doc_id, like=True)
                    st.rerun()

            with col2:
                if st.button(f"Click", key=f"click-{idx}"):
                    update_feedback(doc_id, click=True)
                    st.rerun()

            with col3:
                st.metric("Reward Score", f"{meta.get('score', 0.0):.2f}")

            st.caption(f"Stored on: {meta['timestamp']}")
            st.caption(f"Likes: {meta.get('likes', 0)} | 👁️ Clicks: {meta.get('clicks', 0)}")
