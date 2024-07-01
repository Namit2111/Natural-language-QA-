from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2

#------------------------------------------------ split pdf in text------------------------------------------

# def load_pdf(filename):
#     pdf_file = open(filename, 'rb')

#     pdf_reader = PyPDF2.PdfReader(pdf_file)

#     text = ""
#     for page_num in range( len(pdf_reader.pages)):
#         text += pdf_reader.pages[page_num].extract_text()
#     pdf_file.close()
#     # print(text)
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    
#     documents = text_splitter.split_text(text)

#     return documents

#------------------------------- split pdf in pages-------------------------------
def load_pdf(filename):
    loader = PyPDFLoader(filename)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    documents = text_splitter.split_documents(pages)

    return documents

# if __name__ == "__main__":
#     print(load_pdf("test2.pdf")[0].metadata)