from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "FinSentinel backend running"}


@app.post("/detect-scam")
def detect_scam(message: Message):
    text = message.text.lower()

    strong_indicators = [
        "otp",
        "bank account",
        "account suspended",
        "click here",
        "verify now"
    ]

    medium_indicators = [
        "urgent",
        "blocked",
        "kyc",
        "won",
        "prize",
        "lottery",
        "limited offer",
        "act now",
        "loan approved"
    ]

    score = 0

    for word in strong_indicators:
        if word in text:
            score += 40

    for word in medium_indicators:
        if word in text:
            score += 15

    score = min(score, 95)

    if score >= 70:
        label = "Scam"
        explanation = "High-risk keywords and urgency detected."
    elif score >= 30:
        label = "Suspicious"
        explanation = "Some scam indicators found. Be cautious."
    else:
        label = "Safe"
        explanation = "No strong scam indicators detected."

    return {
        "risk_score": score,
        "label": label,
        "explanation": explanation
    }
