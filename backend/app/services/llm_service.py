
import requests

from app.core.config import OPENROUTER_API_KEY


class OpenRouterService:

    def __init__(self):
        if not OPENROUTER_API_KEY:
            raise ValueError("OpenRouter API key not found. Check your .env file.")

        self.api_key = OPENROUTER_API_KEY
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate_response(self, prompt):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            self.api_url,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]
