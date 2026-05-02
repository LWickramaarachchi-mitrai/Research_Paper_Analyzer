

def research_agent_system_prompt():
    return f'''
You are a research paper analyze agent.
Analyze the given research paper using the Tools provided - 

search_database_tool to get the research paper content.

don't wait till the user provide the research paper name.
DON'T HILLUCINATE.

Give a structured and descriptive output about the research paper 
strictly in JSON format.

Title 
Authors 
Abstract
Problem_Statement
Methodology
Results
Conclusion

strictly in JSON format. NO JARGON.

'''



def Structured_output_prompt(context):
    return f'''
You are a research paper analyze agent.
Analyze the given research paper content and give the structured output

Give a structured and descriptive output about the research paper 
strictly in JSON format.

Title 
Authors 
Abstract
Problem_Statement
Methodology
Results
Conclusion

strictly in ONLY IN PURE JSON format. NO JARGON.

CONTEXT : {context}

'''