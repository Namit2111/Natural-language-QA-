import chromadb
from chromadb.config import Settings
import uuid
def initialize_chromadb():
    """Initialize the ChromaDB client."""
    client = chromadb.PersistentClient(path="./test")
    return client

def get_or_create_collection(chroma_client, collection_name="document_embeddings"):
    """Get or create a collection in ChromaDB."""
    collection = chroma_client.get_or_create_collection(
        name=collection_name
    )
    return collection

def store_embeddings(collection, document_list,embeddings_list,ids_list,metadata_list):
    """Store the document embeddings in ChromaDB."""
    collection.add(
        ids=ids_list,
        documents=document_list,
        embeddings=embeddings_list,
        metadatas=metadata_list
    )


if __name__ == "__main__":
    chroma_client = initialize_chromadb()