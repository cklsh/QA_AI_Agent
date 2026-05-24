from rag.vector_store import VectorStore

store = VectorStore()


def init_knowledge():
    store.load()


def add_knowledge(texts):
    store.add_texts(texts)
    store.save()


def retrieve_context(query):
    return store.search(query)