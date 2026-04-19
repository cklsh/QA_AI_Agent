from rag.vector_store import VectorStore

store = VectorStore()

def load_knowledge():
    docs = [
        "Login should lock after 5 failed attempts",
        "Password must be at least 8 characters",
        "Error messages should be displayed clearly",
        "User session expires after 30 minutes"
    ]

    store.add_texts(docs)

def retrieve_context(query):
    return store.search(query)