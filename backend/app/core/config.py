import os
from pathlib import Path
from dotenv import load_dotenv

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Load .env file
load_dotenv(PROJECT_ROOT / ".env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")