from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import os, shutil, json
from agents.research_agent import analyze_paper_llm_only
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
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