from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
=======
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],   # THIS allows OPTIONS + POST
>>>>>>> 9cb048e1f124b83ef59cdc1e01bab0e2b7e8a733
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

<<<<<<< HEAD
def detect_scam_demo(text: str):
    text = text.lower()

    strong_indicators = ["otp", "bank account", "account suspended"]
    medium_indicators = [
        "blocked", "verify", "urgent", "click",
        "kyc", "won", "prize", "lottery",
        "limited offer", "act now", "loan approved"
    ]

    score = 0

    for w in strong_indicators:
        if w in text:
            score += 40

    for w in medium_indicators:
        if w in text:
            score += 20

    score = min(score, 95)

    if score >= 60:
        return {
            "label": "Scam",
            "risk_score": score,
            "explanation": "Sensitive information and urgency indicate a potential scam."
        }
    else:
        return {
            "label": "Safe",
            "risk_score": 15,
            "explanation": "Message appears normal with no strong scam indicators."
        }

@app.post("/detect-scam")
def detect_scam(data: Message):
    return detect_scam_demo(data.text)
=======
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
>>>>>>> 9cb048e1f124b83ef59cdc1e01bab0e2b7e8a733
