from utils.vector_store import vector_store
from utils.web_search import search_web
from models.llm import generate_response


def answer_query(query, mode="concise"):

    docs = vector_store.search(query)

    # If no relevant documents found → use web search
    if not docs or len(docs) == 0:
        context = search_web(query)
    else:
        context = "\n".join(docs)

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

    return generate_response(prompt)
