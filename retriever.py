from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

def retrieve_for_and_against(claim, k=4, db_dir="db"):
    embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
    db = Chroma(persist_directory=db_dir, embedding_function=embeddings)

    q_for = f"Evidence supporting the claim: {claim}"
    q_against = f"Evidence opposing the claim: {claim}"

    docs_for = db.similarity_search(q_for, k=k)
    docs_against = db.similarity_search(q_against, k=k)

    return docs_for, docs_against
