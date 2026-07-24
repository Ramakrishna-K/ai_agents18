from pydantic import BaseModel

class AgentRequest(BaseModel):
    request: str

class AgentResponse(BaseModel):
    success: bool
    task: list
    output_file: str
    summary: str
