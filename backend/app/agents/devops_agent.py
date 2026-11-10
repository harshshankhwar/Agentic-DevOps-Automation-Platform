
from app.services.llm_service import OpenRouterService


class DevOpsAgent:

    def __init__(self):
        self.name = "DevOps AI Agent"
        self.ai_service = OpenRouterService()

    def analyze_task(self, user_instruction):

        prompt = f"""
        You are an expert DevOps AI Agent.

        Analyze the user's DevOps request.

        User Request: {user_instruction}

        Provide:
        1. Identified DevOps tasks
        2. Step-by-step execution plan
        3. Required tools
        4. Potential risks
        5. Recommendations

        Do not execute any commands.
        Only generate a plan requiring user approval.
        """

        result = self.ai_service.generate_response(prompt)

        return {
            "agent": self.name,
            "user_instruction": user_instruction,
            "AI_generated_plan": result,
            "status": "Plan generated",
            "execution": "Not started - approval required"
        }
