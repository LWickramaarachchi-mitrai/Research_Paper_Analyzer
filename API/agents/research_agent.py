from langchain.agents import create_agent
from langchain_groq import ChatGroq
from prompts import research_agent_system_prompt
from dotenv import load_dotenv
from tools import *
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


input = {"messages":[{"role": "user", "content": "Analyze the given research paper"}]}

result  = research_agent.invoke(input)
print(result)
