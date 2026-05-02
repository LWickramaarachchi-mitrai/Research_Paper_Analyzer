from langchain_groq import ChatGroq
from vectorstore.retriever import retriever
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)


def build_prompt(context, question, chat_history):
    history_text = "\n".join([
        f"{msg['role']}: {msg['content']}"
        for msg in chat_history
    ])

    return f"""
You are an AI assistant answering questions about a research paper.

Use ONLY the provided context.

Chat History:
{history_text}

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""




def chat_with_paper(question: str, chat_history: list):
    
    # 🔍 Retrieve relevant chunks
    context = retriever(question)

    # 🔥 limit context (important)
    context = context[:4000]

    # 🧠 Build prompt
    prompt = build_prompt(context, question, chat_history)

    # 🤖 LLM
    result = llm.invoke(prompt)

    return result.content