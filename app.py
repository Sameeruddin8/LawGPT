import streamlit as st
import os
from flask import Flask, request, render_template
from PyPDF2 import PdfReader   # allows to extract the text from the pdf
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv

load_dotenv()
os.getenv("OPENAI_API_KEY") 
llm = OpenAI(verbose=True)

st.set_page_config(page_title='ASK YOUR PDF')
st.header("ASK YOUR PDF 💬")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new.html')

@app.route('/submit', methods=['POST'])
def submit():
    embeddings = HuggingFaceEmbeddings(model_name = 'intfloat/multilingual-e5-large')
    knowledge_base = FAISS.load_local('embed', embeddings)

    user_question = request.form['user_question']
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
        
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents = docs, question = user_question)
        print(cb)
    return render_template("new.html", response = response)
if __name__ == '__main__':
    app.run(debug=True)