import os
from dotenv import load_dotenv
from groq import Groq

## loading the env file which contains api_key and llama model
load_dotenv()

groq_client  = Groq()

input_path = "chapter1.txt"
output_path = "newtext.txt"

def read_chapter():
    with open(input_path,"r",encoding="utf-8") as f:
        return f.read()
    

def spin_chapter(text):
    prompt = f'''You are an AI writer. Rewrite the following chapter in a more modern and engaging style while preserving its meaning and story.

    --original chapter starts ---
    {text}
    -- original chapter ends---
    Make sure the output reads like a polished novel.

    '''

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
    new_text = spin_chapter(original_text)
    save_new_output(new_text)

