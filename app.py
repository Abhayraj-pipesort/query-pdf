from dotenv import load_dotenv
import os
import openai
from llama_index import VectorStoreIndex, Document
from PyPDF2 import PdfReader
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Ask your PDF")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)

    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    documents = [Document(text=text)]

    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()

    query = st.text_input("Ask your question")

    button = st.button("Ask")

    if button:
        print(query)
        response = query_engine.query(query)
        st.write(response.response)
