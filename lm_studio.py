from pdf_loader import load_pdf
from creat_embeddings import create_embeddings
from store_embeddings import initialize_chromadb,store_embeddings,get_or_create_collection
from search_embeddings import search_embeddings


# ------------------------------------- store embeddings -----------------------------------

# documents  = load_pdf("sql.pdf")

# document_list,embeddings_list,ids_list,metadata_list = create_embeddings(documents)

# chroma_client = initialize_chromadb()

# collection = get_or_create_collection(chroma_client)

# store_embeddings(collection,document_list,embeddings_list,ids_list,metadata_list) 


# ------------------------------------- chat with embeddings -----------------------------------

from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

chroma_client = initialize_chromadb()

collection = get_or_create_collection(chroma_client)

prompt= """ 
You are an helpful agent answer the question only based on the given , if question can not be answered based on given context then dont answer
question :{}
context:{}
"""

history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, just say hi to someone opening this program for the first time. Be concise."},
]

while True:
    completion = client.chat.completions.create(
        model="model-identifier",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)

    print()
    question = input("> ")
    context = search_embeddings(collection, question)
    # print(context["metadatas"])  to get page number of the context
    history.append({"role": "user", "content": prompt.format(question,context["documents"][0][0])})