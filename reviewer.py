import os
from dotenv import load_dotenv
from groq import Groq

## loading the env file which contains api_key and llama model
load_dotenv()

groq_client  = Groq()

input_path = "newtext.txt"
output_path = "review.txt"


def read_chapter():
    with open(input_path,"r",encoding="utf-8") as f:
        return f.read()
    

def review_chapter(text):
    prompt = f"""
    You are an expert AI reviewer. Read the following rewritten chapter and:

    1. Provide 3-5 points of constructive feedback (clarity, tone, consistency).
    2. Suggest improvements.
    3. Rewrite the chapter with those improvements applied.

    --- Rewritten Chapter Start ---
    {text}
    --- Rewritten Chapter End ---
    """


    responce = groq_client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.8,
        model=os.environ['GROQ_MODEL']
    )

    return responce.choices[0].message.content

def save_new_output(content):
    with open(output_path,"w",encoding="utf-8") as f:
        f.write(content)

    print("saved the new content..")

if __name__=="__main__":

    original_text = read_chapter()
    reviewed_text = review_chapter(original_text)
    save_new_output(reviewed_text)

