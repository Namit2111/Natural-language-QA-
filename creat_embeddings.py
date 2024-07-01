from langchain_huggingface import HuggingFaceEmbeddings

def create_embeddings(documents,filename = "test"):
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    document_list = []
    embeddings_list = []
    ids_list = []
    metadata_list = []
    for i,doc in enumerate(documents):
        embedding = embeddings_model.embed_query(doc.page_content)
        # document_embeddings.append({
        #     'text': doc.page_content,
        #     'embedding': embedding
        # })
        document_list.append(doc.page_content)
        embeddings_list.append(embedding)
        ids_list.append(f"{filename}_{i}")
        metadata_list.append(doc.metadata)
    return document_list,embeddings_list,ids_list,metadata_list

