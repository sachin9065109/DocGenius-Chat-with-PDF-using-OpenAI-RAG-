import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


# -------------------- Configuration -------------------- #
load_dotenv()

API_KEY = os.getenv("GEMINI_API")

if not API_KEY:
    st.error("Gemini API key not found. Please configure your .env file.")
    st.stop()

genai.configure(api_key=API_KEY)


# -------------------- Helper Function -------------------- #
def generate_response(prompt: str) -> str:
    """
    Generate response using Gemini model.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(prompt)
    return result.text


# -------------------- Streamlit UI -------------------- #
st.set_page_config(
    page_title="DocGenius",
    page_icon="📄",
    layout="centered",
)

st.title("📄 DocGenius")
st.subheader("AI-Powered Content Generator")

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Ask anything...",
    height=120,
)

if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response..."):
            answer = generate_response(prompt)

        st.success("Response Generated")
        st.markdown(answer)
