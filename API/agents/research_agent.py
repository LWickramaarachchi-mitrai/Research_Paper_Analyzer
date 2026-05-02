from langchain.agents import create_agent
from langchain_groq import ChatGroq
from agents.prompts import *
from dotenv import load_dotenv
from agents.tools import *
from agents.structured_output import *
from vectorstore.retriever import save_file
import json
load_dotenv()


llm_structured = ChatGroq(
    model="openai/gpt-oss-120b",
    response_format={"type": "json_object"}
)


research_system_prompt = research_agent_system_prompt()



def analyze_paper_llm_only(file_path: str):
    save_file(file_path)
    context = multi_step_retrieval(search_database_tool)
    
    prompt = Structured_output_prompt(context)
    
    result = llm_structured.invoke(prompt)

    data = json.loads(result.content)

    parsed = ResearchPaper(**data)
    

    return parsed

#res = analyze_paper_llm_only("./test_docs/bert.pdf")
#print(res)





