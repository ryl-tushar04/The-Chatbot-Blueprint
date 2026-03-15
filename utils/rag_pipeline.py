from utils.vector_store import VectorStore
from utils.web_search import search_web
from models.llm import generate_response

vector_store = VectorStore()
def add_documents(chunks):
    vector_store.add_documents(chunks)
def answer_query(query, mode="concise", provider="openai"):
    docs = vector_store.search(query)
    if not docs:
        context = search_web(query)
    else:
        context = "\n".join(docs)
    if len(context.strip()) == 0:
        context = search_web(query)
    if mode == "concise":
        instruction = "Answer briefly in 3-4 lines."
    else:
        instruction = "Provide a detailed explanation."
    prompt = f"""
    Use the following context to answer the question.

    Context:
    {context}
    Question:
    {query}
    Instruction:
    {instruction}
    """
    return generate_response(prompt, provider)