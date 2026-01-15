from langchain_community.vectorstores import Chroma # type: ignore
from langchain_community.embeddings import OllamaEmbeddings # type: ignore

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)

# Total number of stored chunks
print("Number of documents in DB:", db._collection.count())
