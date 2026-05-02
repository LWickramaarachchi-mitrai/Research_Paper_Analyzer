from pydantic import BaseModel, Field

class ResearchPaper(BaseModel):
    title: str = Field(description="Include the Research Paper Name")
    authors: list[str] = Field(description="Include Authors of the given research paper")
    abstract: str = Field(description="Include the Full Abstract of the given research paper")
    problem_statement: str = Field(description="Include the problem Statement address in the given research paper")
    methodology: str = Field(description="Include the methodolgy states in the given research paper")
    results: str = Field(description="Include the full Results in the given research paper")
    conclusion: str = Field(description="Include the final Conclusion given research paper")
    
    
