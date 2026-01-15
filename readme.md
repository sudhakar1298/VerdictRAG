# VerdictRAG

VerdictRAG is a Retrieval-Augmented Generation (RAG) system designed for legal reasoning. It takes a user-submitted claim, retrieves relevant evidence both supporting and opposing the claim from a legal document, and uses a Large Language Model (LLM) to generate a balanced, structured argument.

The core of this system is its unique retrieval strategy, which actively seeks out conflicting information to provide a more nuanced and comprehensive analysis than a standard RAG pipeline.

## How It Works

The system operates in three main stages:

1.  **Ingestion**: A source PDF document (e.g., a legal text, case file, or statute) is loaded, split into manageable chunks, and processed using `nomic-embed-text` embeddings. These vectorized chunks are then stored in a ChromaDB vector database for efficient retrieval.

2.  **Dual-Query Retrieval**: When a user enters a claim, the system generates two distinct queries:
    *   A query to find evidence *supporting* the claim.
    *   A query to find evidence *opposing* the claim.

    It then performs similarity searches for both queries against the vector database, collecting separate sets of documents for each side of the argument.

3.  **Argument Generation**: The original claim, along with the retrieved supporting and opposing evidence, is formatted into a detailed prompt. This prompt instructs a `llama3` model to act as a legal reasoning assistant. The model then generates a structured response that includes:
    *   Arguments Supporting the Claim
    *   Arguments Against the Claim
    *   A balanced Conclusion based *only* on the provided evidence.

## Setup and Usage

### Prerequisites

*   Python 3.8+
*   [Ollama](https://ollama.com/) installed and running.

### 1. Installation

Clone the repository and install the required Python dependencies:

```bash
git clone https://github.com/sudhakar1298/verdictrag.git
cd verdictrag
pip install langchain langchain_community langchain_core langchain_ollama langchain_chroma pypdf
````

### 2. Set Up Ollama Models

Pull the necessary embedding and generation models for Ollama:

```bash
ollama pull nomic-embed-text
ollama pull llama3
```

### 3. Ingest Data

1.  Place your source legal document in the `data/` directory. The ingestion script is currently hardcoded to use `data/repealedfileopen.pdf`.
2.  Run the ingestion script to build the vector database. This will create a `db/` directory containing the index.

```bash
python ingest.py
```

You can verify the contents of the database using the inspection script:

```bash
python inspect_db.py
```

### 4. Run the Application

Execute the main application script. It will prompt you to enter a legal claim.

```bash
python app.py
```

The system will then process your claim and print the structured legal analysis to the console.

**Example Interaction:**

```
Enter your claim: [Your legal claim here]

--- RAG Lawyer Response ---

1. Arguments Supporting the Claim
...

2. Arguments Against the Claim
...

3. Conclusion
...
```

## Project Structure

*   `ingest.py`: Handles loading, chunking, and indexing the source PDF into the Chroma vector database.
*   `retriever.py`: Contains the `retrieve_for_and_against` function, which performs the dual-query search for supporting and opposing evidence.
*   `lawyer.py`: Contains the `argue` function, which prompts the LLM with the claim and retrieved evidence to generate the final structured argument.
*   `app.py`: The main entry point for the application. It orchestrates the retrieval and generation process based on user input.
*   `inspect_db.py`: A utility script to count the number of documents in the vector database.
*   `data/`: Directory for source documents.