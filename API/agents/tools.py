import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from langchain.tools import tool
from vectorstore.retriever   import retriever

@tool
def search_database_tool(query: str):
    '''
    use this tool to Get the information of the
    resarch paper.
    
    Do Not hillucinate
    
    Args:
        query: Search the query term that you looking for
    
    '''
    print("Database tool executing.....")
    result = retriever(query)
    return result;

#multi step reasoning tool

def multi_step_retrieval(retriever_tool):
    sections = {
        "title": "Research paper Name",
        "authors": "Authors of the given Research paper ",
        "abstract": "abstract of the research paper with title",
        "problem_statement": "problem adddressed in the paper",
        "methodology": "methodolgy states in the given research paper",
        "results": "Include the full Results in the given research paper",
        "conclution": "results performance evaluation findings Include the final Conclusion given research paper"
    }

    results = {}
    
    print("multi step retrievel started.....")

    for key, query in sections.items():
        result = retriever_tool.invoke(query)

        # Optional refinement (if weak result)
        if len(result) < 200:
            result += "\n" + retriever_tool.invoke(query + " in detail")

        results[key] = result
        
    print("multi step retrievel completed!")

    return results