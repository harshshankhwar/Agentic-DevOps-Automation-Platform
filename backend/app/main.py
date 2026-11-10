
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Agentic DevOps Automation Platform",
    description="AI-powered DevOps automation system",
    version="1.0.0"
)

app.include_router(router)

