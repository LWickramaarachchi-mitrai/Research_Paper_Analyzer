from langchain.agents import create_agent
from langchain_groq import ChatGroq
from prompts import *
from dotenv import load_dotenv
from tools import *
from structured_output import *
from vectorstore.retriever import save_file
load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)



research_agent_tools = [search_database_tool]

llm_with_tools = llm.bind_tools(research_agent_tools)


research_system_prompt = research_agent_system_prompt()


research_agent = create_agent(
    model=llm_with_tools,
    tools = research_agent_tools,
    system_prompt = research_system_prompt
)


def analyze_paper(paper_path: str,query: str):
    save_file(paper_path)
    input = {"messages":[{"role": "user", "content": query}]}
    result  = research_agent.invoke(input)
    context = result['messages'][-1].content

    return context

res = analyze_paper("./test_docs/attention.pdf", "Analyze the given research paper")
print(res)





