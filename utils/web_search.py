from tavily import TavilyClient
import os
import streamlit as st

api_key = st.secrets.get("TAVILY_API_KEY", os.getenv("TAVILY_API_KEY"))
client = TavilyClient(api_key=api_key)
def search_web(query):
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )
    results = []
    for r in response["results"]:
        results.append(r["content"])

    return "\n".join(results)
