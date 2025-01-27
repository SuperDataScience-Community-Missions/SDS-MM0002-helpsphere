# basic imports
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import gradio as gr
import torch
import glob
import os

load_dotenv()

# Langchain imports
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_core.callbacks import StdOutCallbackHandler

def read_docs():
    folder = '../company-files'
    loader = DirectoryLoader(folder, glob="*.txt", loader_cls=TextLoader)
    docs = loader.load()
    return docs

def chunk_docs(docs):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    return chunks

def creating_vectorstore(chunks):
    
    db_name = "vector_db"
    embeddings = OpenAIEmbeddings()

    # delete if vectorstore already exists
    if os.path.exists(db_name):
        Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_name)
    return vectorstore

def chatbot(query, history):

    result = conversation_chain.invoke({"question":query})
    return result["answer"]




# Main logic
docs = read_docs()
chunks = chunk_docs(docs)
vectorstore = creating_vectorstore(chunks)

llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
retriever = vectorstore.as_retriever(search_kwargs={'k':3})
conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory, callbacks=[StdOutCallbackHandler()])

gr.ChatInterface(chatbot, type="messages").launch(inbrowser=True)