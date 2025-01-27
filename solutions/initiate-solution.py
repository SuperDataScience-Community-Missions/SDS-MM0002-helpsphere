from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import gradio as gr

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
client = InferenceClient(api_key=HUGGINGFACE_API_KEY)

system_message = """
You are a helpful customer service assistant and will answer questions pretaining to a fictional
e-commerce company called TechStyle Global.

You are to act the best customer service representative and help the user with any queries
they have. Keep your tone formal and cheerful.
"""

def select_language():
    print("\nPlease select your preferred language:")
    languages = ["English", "Spanish", "French", "German"]
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")
    
    choice = int(input("\nSelect language number: "))
    return languages[choice-1]

lang = select_language()

system_message += f" Reply to the user in {lang}"

prompt = input("You: ")
messages = [
    {"role":"assistant","content":system_message},
    {"role":"user","content":prompt}
]

stream = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct", 
    messages=messages, 
    max_tokens=500,
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
