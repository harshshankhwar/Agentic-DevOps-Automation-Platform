
from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.devops_agent import DevOpsAgent

router = APIRouter()

# Initialize AI Agent
agent = DevOpsAgent()


# Request model
class AgentRequest(BaseModel):
    instruction: str


# Home API
@router.get("/")
def home():
    return {
        "message": "Welcome to Agentic DevOps Automation Platform!",
        "status": "Running"
    }


# Health Check API
@router.get("/health")
def health_check():
    return {
        "status": "Healthy"
    }


# Project Information API
@router.get("/project")
def project_info():
    return {
        "project": "Agentic AI-Based DevOps Automation Platform",
        "version": "1.0.0",
        "features": [
            "AI Agent",
            "Code Analysis",
            "Automated Testing",
            "DevOps Automation"
        ]
    }


# AI Agent API
@router.post("/agent/plan")
def create_agent_plan(request: AgentRequest):

    result = agent.analyze_task(request.instruction)

    return result
