from fastapi import APIRouter

router = APIRouter()

@router.post("/sentiment")
def sentiment_endpoint(text: str):
    text_lower = text.lower()
    if "good" in text_lower:
        return {"sentiment": "positive"}
    elif "bad" in text_lower:
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}
