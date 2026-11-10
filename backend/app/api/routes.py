
import requests

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.agents.devops_agent import DevOpsAgent
from app.services.github_service import GitHubService
from app.services.code_analyzer import CodeAnalyzer


router = APIRouter()

# Initialize Services
agent = DevOpsAgent()
github_service = GitHubService()
code_analyzer = CodeAnalyzer()


# Request Models
class AgentRequest(BaseModel):
    instruction: str


class GitHubAnalysisRequest(BaseModel):
    owner: str
    repo: str
    path: str


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
            "GitHub Integration",
            "Automated Testing",
            "DevOps Automation"
        ]
    }


# AI Agent API
@router.post("/agent/plan")
def create_agent_plan(request: AgentRequest):

    result = agent.analyze_task(request.instruction)

    return result


# GitHub Code Analysis API
@router.post("/github/analyze")
def analyze_github_code(request: GitHubAnalysisRequest):

    try:
        # Fetch code from GitHub
        source_code = github_service.get_file_content(
            request.owner,
            request.repo,
            request.path
        )

        # Analyze source code
        analysis_result = code_analyzer.analyze_code(source_code)

        return {
            "repository": f"{request.owner}/{request.repo}",
            "file": request.path,
            "analysis": analysis_result
        }

    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Unable to fetch file from GitHub."
        )

    except (ValueError, KeyError) as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
