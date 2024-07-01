# README

## Project Overview

This project aims to develop a system that can take in a natural language query and output an answer in a conversational style. The system utilizes pre-trained language models, embeddings, and a vector database to store and search embeddings of documents for relevant information. The primary components of this project include loading documents, creating embeddings, storing and searching embeddings, and generating responses based on the embeddings.

## Features

- **Document Loading**: Load and split PDF documents into manageable chunks.
- **Embeddings Creation**: Generate embeddings for document chunks using a pre-trained model.
- **Embeddings Storage**: Store embeddings in a ChromaDB database.
- **Query Handling**: Search for relevant document chunks based on a query and generate a response using a language model.
- **Conversational Interface**: Interact with the system through a simple conversational interface.

## Setup and Installation

1. **Clone the Repository**:

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

## Design Notes

### Intermediary Representation

To effectively organize raw data from web articles and PDF documents into a structured format for storage and consumption by language models, the following approach was taken:

1. **Text Splitting**: PDF documents are split into smaller chunks of text to facilitate efficient embedding creation and storage.
2. **Embeddings**: Each chunk of text is converted into an embedding using a pre-trained model (`all-MiniLM-L6-v2`).
3. **Metadata Storage**: Alongside embeddings, metadata for each document chunk (e.g., page number) is stored to maintain context.

### Open Source Libraries and Tools

- **LangChain**: Used for text splitting and document loading.
- **HuggingFace Embeddings**: Utilized for creating embeddings from document chunks.
- **ChromaDB**: Employed for storing and searching embeddings.
- **OpenAI**: Used for generating conversational responses.
