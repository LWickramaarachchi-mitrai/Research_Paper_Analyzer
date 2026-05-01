from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from rank_bm25 import BM25
from sentence_transformers import CrossEncoder
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def save_file(file_path: str):
    loader = PyPDFLoader(file_path=file_path)
    file = loader.load()
    
    splitter  = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100);
    chunked_doc = splitter.split_documents(file)
    vectorstore = FAISS.from_documents(chunked_doc, embeddings)
    vectorstore.save_local("FAISS_INDEX")
  
 
def retriever(query: str):
    initial_load = FAISS.load_local("FAISS_INDEX", embeddings=embeddings, allow_dangerous_deserialization=True)
    sementic_results = initial_load.similarity_search(query, k = 5);
    
    pairs = [(query,i.page_content)  for i in sementic_results]
    rank_score = reranker.predict(pairs)
    scored_results = list(zip(sementic_results, rank_score))
    scored_results.sort(key = lambda x:x[1], reverse=True)
    
    top_docs = [doc for doc,score  in scored_results[:3]]
    
    results = "/n".join([i.page_content for i in top_docs])
    return results;

    
    
    
    

#save_file("./test_docs/attention.pdf")
#results = retriever("Attention Mechanism")
#print(results)
    
    
