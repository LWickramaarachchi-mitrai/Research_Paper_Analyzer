from fastapi import FastAPI, UploadFile, File, Form,Body
from pydantic import BaseModel
import os, shutil, json
from agents.research_agent import analyze_paper_llm_only
from agents.chat_with_paper import graph
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import HumanMessage
from langchain_core.messages import HumanMessage, AIMessage
from services.ChatMemory import save_message, get_chat_history

load_dotenv()


from vectorstore.retriever import save_file





app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---- request schema ----
class AnalyzeRequest(BaseModel):
    query: str
    
    
    



# ---- upload endpoint ----
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    save_file(file_path)

    return {"message": f"{file.filename} indexed successfully"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    #query: str = Form(...)
):
    try:
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Index (optional optimization later)
        #save_file(file_path)

        # Run analysis
        result = analyze_paper_llm_only(file_path)

        return result

    except Exception as e:
        return {
            "error": str(e)
        }
        



class ChatRequest(BaseModel):
    message: str
    thread_id: str


@app.post("/chat")
async def chat(req: ChatRequest):

    # ✅ Load history from MongoDB
    history = get_chat_history(req.thread_id)

    # Convert to LangChain messages
    messages = []
    for m in history:
        if m["role"] == "user":
            messages.append(HumanMessage(content=m["content"]))
        else:
            messages.append(AIMessage(content=m["content"]))

    # Add new user message
    messages.append(HumanMessage(content=req.message))

    # Invoke LangGraph
    result = graph.invoke(
        {"messages": messages},
        config={"configurable": {"thread_id": req.thread_id}}
    )

    response = result["messages"][-1].content

    # ✅ Save to MongoDB
    save_message(req.thread_id, "user", req.message)
    save_message(req.thread_id, "assistant", response)

    return {"response": response}