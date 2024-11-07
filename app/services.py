import requests
from app.models import StudentSummary

OLLAMA_API_URL = "http://localhost:11411/v1/llama"  # Change this if your Ollama setup uses a different port

def generate_student_summary(student_name: str, student_age: int, student_email: str) -> StudentSummary:
    prompt = f"Provide a summary for the student named {student_name}, age {student_age}, and email {student_email}."
    
    # Make API request to Ollama
    response = requests.post(
        OLLAMA_API_URL,
        json={"model": "llama3", "input": prompt}
    )
    
    if response.status_code == 200:
        data = response.json()
        return StudentSummary(summary=data["text"])
    else:
        raise Exception(f"Ollama API error: {response.status_code} - {response.text}")
