from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import gradio as gr
import torch

load_dotenv()

def get_docs():
    filenames = []
    for filename in os.listdir('company-files'):
        filenames.append(filename)

    return filenames

def get_relevant_context(prompt):
    relevant_context = []
    filenames = get_docs()
    for filename in filenames:
        if filename.replace('.txt','') in prompt:
            with open('company-files/' + filename, 'r') as file:
                context = file.read()
                relevant_context.append(context)
    return relevant_context

def add_relevant_context(prompt):
    relevant_context = get_relevant_context(prompt)
    if relevant_context:
        prompt += "/n/nThe following information might be relevant to answering this question:/n/n"
        for context in relevant_context:
            prompt += context + "/n/n"

    return prompt

def chatbot(message, history):
    system_message = """
    You are a helpful customer service assistant whose name is Rachel and will answer questions 
    pretaining to a fictional e-commerce company called TechStyle Global.

    You are to act the best customer service representative and help the user with any queries
    they have. Keep your tone formal and cheerful.

    If you receive a blank or gibberish input from the user, ask the user to give a valid question.

    Do not make anything up yourself. If you do not know the ansewr to a question, clearly say so.

    Do not thank the user for giving you any information.

    Keep your responses short and concise.
    """
    messages = [{"role":"assistant","content":system_message}] + history
    message = add_relevant_context(message)
    messages.append({"role":"user","content":message})

    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    client = InferenceClient(api_key=HUGGINGFACE_API_KEY)

    stream = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct", 
        messages=messages, 
        max_tokens=500,
        stream=True
    )

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content
        yield response

gr.ChatInterface(
    fn=chatbot,
    type="messages",
    title="Chatbot Interface"
).launch()