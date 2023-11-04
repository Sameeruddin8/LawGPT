import streamlit as st
import os
from PyPDF2 import PdfReader   # allows to extract the text from the pdf
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv


load_dotenv()
os.getenv("OPENAI_API_KEY") 

pdf = 'Data/Resume.pdf'
if pdf is not None:
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    #Split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )

    chunks = text_splitter.split_text(text)
    
    #creating embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    knowledge_base.save_local('embed')
