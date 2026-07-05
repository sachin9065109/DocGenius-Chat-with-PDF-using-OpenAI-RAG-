import streamlit as st
from dotenv import load_dotenv

from src.pdf_loader import load_pdf_text
from src.vector_store import build_vector_store
from src.chatbot import ask_question

load_dotenv()

st.set_page_config(
    page_title="DocGenius",
    page_icon="📄",
    layout="wide"
)

st.title("📄 DocGenius")
st.caption("AI-powered PDF Question Answering System")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("Processing document..."):
        document_text = load_pdf_text(uploaded_file)
        vector_db = build_vector_store(document_text)

    st.success("Document processed successfully.")

    question = st.text_input("Ask a question")

    if question:
        with st.spinner("Generating answer..."):
            answer = ask_question(question, vector_db)

        st.markdown("### Answer")
        st.write(answer)
