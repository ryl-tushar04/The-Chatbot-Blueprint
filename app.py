import streamlit as st
from pypdf import PdfReader
from utils.document_loader import split_documents
from utils.rag_pipeline import add_documents, answer_query

st.title("AI Chatbot Blueprint")
st.sidebar.title("Settings")
provider = st.sidebar.selectbox(
    "Choose LLM Provider",
    ["Llama 3"]
)
mode = st.sidebar.radio(
    "Response Mode",
    ["concise", "detailed"]
)
uploaded_file = st.sidebar.file_uploader(
    "Upload knowledge file",
    type=["txt", "pdf"]
)
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    else:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
    chunks = split_documents(text)
    add_documents(chunks)
    st.sidebar.success("Document added")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
query = st.chat_input("Ask something")
if query:
    st.chat_message("user").write(query)
    response = answer_query(query, mode)
    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "user", "content": query})
    st.session_state.messages.append({"role": "assistant", "content": response})
