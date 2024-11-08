from langchain_huggingface import HuggingFaceEmbeddings
from utils.store_embeddings import initialize_chromadb,get_or_create_collection
def search_embeddings(collection, query,assertID):
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    query_embedding = embeddings_model.embed_query(query)
    results = collection.query(query_embeddings=query_embedding, n_results=1,include=["documents","metadatas"],where={"assertID": {"$eq": assertID}})
    return results

if __name__ == "__main__":
    c = initialize_chromadb()
    cp = get_or_create_collection(c,collection_name="prompts")
    print(search_embeddings(collection=cp, query="asas"))