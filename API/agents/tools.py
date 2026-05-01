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
    result = retriever(query)
    return result;