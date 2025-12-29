from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/detect-scam")
def detect_scam(message: Message):
    text = message.text.lower()

    if "click" in text or "urgent" in text or "blocked" in text:
        return {
            "risk_score": 90,
            "label": "Scam",
            "explanation": "The message creates urgency and asks the user to take immediate action, which is common in scams."
        }

    return {
        "risk_score": 10,
        "label": "Safe",
        "explanation": "The message does not show common scam patterns like urgency or malicious links."
    }
