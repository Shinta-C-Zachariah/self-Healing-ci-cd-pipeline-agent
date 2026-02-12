import openai
from logger import log_action

openai.api_key = "YOUR_OPENAI_API_KEY"

def ai_suggest_fix(error_message):
    """
    Agentic AI suggests a fix for unknown errors.
    """
    prompt = f"""
    You are a DevOps assistant. A GitHub Actions CI/CD pipeline failed with the following error:
    {error_message}
    Suggest a Python or shell command to fix it.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        suggestion = response.choices[0].message.content.strip()
        log_action(f"AI suggested fix: {suggestion}")
        return suggestion
    except Exception as e:
        log_action(f"AI reasoning failed: {e}")
        return None
