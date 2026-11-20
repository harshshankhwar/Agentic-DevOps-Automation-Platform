
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from app.api.routes import router

app = FastAPI(
    title="Agentic DevOps Automation Platform",
    description="AI-powered DevOps automation system",
    version="1.0.0"
)

# Static files directory
STATIC_DIR = Path(__file__).resolve().parent / "static"

# Serve CSS and JavaScript
app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)

# API routes
app.include_router(router)


# Frontend Dashboard
@app.get("/dashboard", include_in_schema=False)
def dashboard():
    return FileResponse(STATIC_DIR / "index.html")
