from fastapi import FastAPI

app = FastAPI(
    title="Agentic DevOps Automation Platform",
    description="AI-powered DevOps automation system",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Agentic DevOps Automation Platform!",
        "status": "Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "Healthy"
    }