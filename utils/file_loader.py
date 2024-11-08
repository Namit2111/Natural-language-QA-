from langchain_community.document_loaders import PyPDFLoader,TextLoader,Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2




def load_pdf(filename):
    loader = PyPDFLoader(filename)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    documents = text_splitter.split_documents(pages)

    return documents

def load_txt(filename):
    loader = TextLoader(filename)
    doc = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    documents = text_splitter.split_documents(doc)

    return documents

def load_docx(filename):
    
    loader = Docx2txtLoader(filename)
    doc = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    documents = text_splitter.split_documents(doc)

    return documents

import os

def load_file(filename):
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == '.pdf':
        return load_pdf(filename)

    elif file_extension == '.txt':
        return load_txt(filename)

    elif file_extension == '.docx':
        return load_docx(filename)

    else:
        raise ValueError(f"Unsupported file type: {file_extension}")



if __name__ == "__main__":
    print(load_docx("test.docx"))