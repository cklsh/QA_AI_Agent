import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


class VectorStore:
    def __init__(
        self,
        index_path="rag/faiss.index",
        meta_path="rag/texts.pkl"
    ):
        self.index_path = index_path
        self.meta_path = meta_path

        self.index = None
        self.texts = []

    def add_texts(self, texts):
        embeddings = model.encode(texts)

        embeddings = np.array(embeddings).astype("float32")

        if self.index is None:
            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query, k=3):
        if self.index is None:
            return []

        query_embedding = model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for idx in indices[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])

        return results

    def save(self):
        if self.index:
            faiss.write_index(self.index, self.index_path)

            with open(self.meta_path, "wb") as f:
                pickle.dump(self.texts, f)

    def load(self):
        try:
            self.index = faiss.read_index(self.index_path)

            with open(self.meta_path, "rb") as f:
                self.texts = pickle.load(f)

            print("✅ RAG memory loaded")

        except:
            print("⚠️ No existing RAG memory found")