import faiss
import numpy as np
from models.embeddings import embed_text

class VectorStore:
    def __init__(self):
        self.texts = []
        self.index = None
    def add_documents(self, docs):
        if not docs:
            return
        embeddings = embed_text(docs)
        if len(embeddings) == 0:
            return
        dim = len(embeddings[0])
        if self.index is None:
            self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))
        self.texts.extend(docs)
    def search(self, query, k=3):
        if self.index is None:
            return []
        query_embedding = embed_text([query])
        distances, indices = self.index.search(np.array(query_embedding), k)
        results = []
        for idx in indices[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])
        return results