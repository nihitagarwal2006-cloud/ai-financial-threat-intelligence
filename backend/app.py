@app.post("/detect-scam")
def detect_scam(message: Message):
    text = message.text.lower()

    score = 0

    # Strong scam indicators
    strong_patterns = [
        "bank account",
        "suspended",
        "click",
        "verify",
        "otp",
        "payment",
        "transfer",
        "prize",
        "lottery",
        "won",
        "urgent",
        "limited offer",
        "act now",
        "guaranteed",
        "loan approved",
        "kyc",
        "refund",
        "cashback"
    ]

    # Detect links
    if "http://" in text or "https://" in text or "bit.ly" in text or "tinyurl" in text:
        score += 35

    # Detect urgency patterns
    urgency_words = ["urgent", "immediately", "now", "24 hours", "suspended"]
    for word in urgency_words:
        if word in text:
            score += 20

    # Detect strong keywords
    for word in strong_patterns:
        if word in text:
            score += 15

    # Cap score
    score = min(score, 95)

    if score >= 75:
        label = "Scam"
        explanation = "Multiple high-risk indicators detected including urgency or suspicious links."
    elif score >= 40:
        label = "Suspicious"
        explanation = "Some scam-related patterns detected. Proceed with caution."
    else:
        label = "Safe"
        explanation = "No major scam indicators detected."

    return {
        "risk_score": score,
        "label": label,
        "explanation": explanation
    }
