import streamlit as st
import os


GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
