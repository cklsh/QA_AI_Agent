import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def __init__(self):
        self.texts = []
        self.index = None

    def add_texts(self, texts):
        embeddings = model.encode(texts)

        if self.index is None:
            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(np.array(embeddings))
        self.texts.extend(texts)

    def search(self, query, k=3):
        if self.index is None:
            return []

        query_vec = model.encode([query])
        distances, indices = self.index.search(query_vec, k)

        results = []
        for i in indices[0]:
            if i < len(self.texts):
                results.append(self.texts[i])

        return results