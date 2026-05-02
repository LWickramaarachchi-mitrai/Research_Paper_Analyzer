from langchain_community.vectorstores import Chroma
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import pickle

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def save_file(file_path: str):
    loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()

    for doc in documents:
        doc.metadata["source"] = file_path

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunked_doc = splitter.split_documents(documents)

    # -------- VECTOR STORE --------
    vectorstore = Chroma(
        persist_directory="CHROMA_DB",
        embedding_function=embeddings
    )
    vectorstore.add_documents(chunked_doc)
    vectorstore.persist()

    # -------- BM25 --------
    texts = [doc.page_content for doc in chunked_doc]
    tokenized_corpus = [text.split() for text in texts]

    bm25 = BM25Okapi(tokenized_corpus)

    # save BM25 + docs
    with open("bm25.pkl", "wb") as f:
        pickle.dump((bm25, chunked_doc), f)
  
 
def retriever(query: str):
    # -------- LOAD VECTOR DB --------
    vectorstore = Chroma(
        persist_directory="CHROMA_DB",
        embedding_function=embeddings
    )

    semantic_results = vectorstore.similarity_search(query, k=5)

    # -------- LOAD BM25 --------
    with open("bm25.pkl", "rb") as f:
        bm25, docs = pickle.load(f)

    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    # get top BM25 docs
    bm25_top_indices = sorted(
        range(len(bm25_scores)),
        key=lambda i: bm25_scores[i],
        reverse=True
    )[:5]

    bm25_results = [docs[i] for i in bm25_top_indices]

    # -------- MERGE RESULTS --------
    combined_docs = semantic_results + bm25_results

    # remove duplicates
    seen = set()
    unique_docs = []
    for doc in combined_docs:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            unique_docs.append(doc)

    # -------- RERANK --------
    pairs = [(query, doc.page_content) for doc in unique_docs]
    scores = reranker.predict(pairs)

    scored_results = list(zip(unique_docs, scores))
    scored_results.sort(key=lambda x: x[1], reverse=True)

    top_docs = [doc for doc, _ in scored_results[:3]]

    results = "\n".join([
        f"[{doc.metadata.get('source')}]\n{doc.page_content}"
        for doc in top_docs
    ])

    return results
    
    
    


#save_file("./test_docs/attention.pdf")
#results = retriever("Attention architecture")
#print(results)
    
    
