from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_groq import ChatGroq
from agents.states import GraphState
from vectorstore.retriever import retriever
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import AIMessage
from langgraph.graph import StateGraph, END
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

conn = sqlite3.connect("chat_memory.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

llm = ChatGroq(model="openai/gpt-oss-120b")


def chat_node(state: GraphState):
    messages = state["messages"]
    user_query = messages[-1].content

   
    context = retriever(user_query)

    

    system_prompt = f"""
You are a research assistant.

Use the context to answer.
If not found, say you don't know.

Context:
{context}
"""

    response = llm.invoke([
        {"role": "system", "content": system_prompt},
        *messages
    ])

    return {
        "messages": messages + [response]
    }
    



builder = StateGraph(GraphState)

builder.add_node("chat", chat_node)

builder.set_entry_point("chat")
builder.add_edge("chat", END)

graph = builder.compile(checkpointer=checkpointer)