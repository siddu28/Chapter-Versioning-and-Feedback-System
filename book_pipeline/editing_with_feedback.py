import os
from dotenv import load_dotenv
from groq import Groq

## loading the env file which contains api_key and llama model
load_dotenv()

groq_client  = Groq()

review_path = "review.txt"
editor_feedback_path = "editor_feedback.txt"
final_output_path = "final_text.txt"


def read_feedback():
    with open(editor_feedback_path, "r", encoding="utf-8") as f:
        return f.read()

def read_reviewed_chapter():
    with open(review_path, "r", encoding="utf-8") as f:
        return f.read()
    
    

def apply_feedback(reviewed_text,feedback):
    prompt = f"""
    You are an expert editor. Here's the previously improved chapter:

    --- Reviewed Chapter ---
    {reviewed_text}

    And here is human feedback for further improvement:

    --- Editor Feedback ---
    {feedback}

    Now apply the feedback and rewrite the chapter accordingly.
    Only output the final improved chapter.
    """


    responce = groq_client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.7,
        model=os.environ['GROQ_MODEL']
    )

    return responce.choices[0].message.content

def save_final_version(text):
    with open(final_output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Final version saved to", final_output_path)


if __name__ == "__main__":
    reviewed_text = read_reviewed_chapter()
    editor_feedback = read_feedback()
    improved_text = apply_feedback(reviewed_text, editor_feedback)
    save_final_version(improved_text)