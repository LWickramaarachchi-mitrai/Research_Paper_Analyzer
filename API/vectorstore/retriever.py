from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain_text_splitters import RecursiveCharacterTextSplitter

""" model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(
    model_name=model_name
) """



""" def retriever(file):
    loader = PyPDFLoader(file_path= file)
    pdf = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
    chunked_doc = splitter.split_documents(pdf)
    vectorstore = FAISS.from_documents(chunked_doc, embeddings) """
    
    
    
