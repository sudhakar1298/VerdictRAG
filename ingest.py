from langchain_community.document_loaders import PyPDFLoader,DocklingLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

def build_index(
    chunk_size=400,
    chunk_overlap=50,
    embed_model="nomic-embed-text:latest",
    persist_dir="db"
):
    loader = DocklingLoader("data/repealedfileopen.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(docs)

    print("Chunks created:", len(chunks))

    embeddings = OllamaEmbeddings(model=embed_model)

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=persist_dir
    )

    print(f"Indexed {len(chunks)} chunks into '{persist_dir}'")

if __name__ == "__main__":
    build_index()
