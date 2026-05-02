from pydantic import BaseModel

class ResearchPaper(BaseModel):
    title: str
    authors: str
    abstract: str
    problem_statement: str
    methodology: str
    results: str
    conclusion: str