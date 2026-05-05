

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

strictly  ONLY IN PURE JSON format. NO JARGON.

'''






def Structured_output_prompt(context):
    return f"""
Extract structured information from the research paper.

Rules:
- Keep each field concise (max 2–3 sentences)
- Return ONLY valid JSON
- Do NOT exceed output length

Schema:
{{
  "title": "",
  "authors": [],
  "abstract": "",
  "problem_statement": "",
  "methodology": "",
  "results": "",
  "conclusion": ""
}}

Paper:
{context}
"""