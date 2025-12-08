from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@router.post("/sentiment")
def sentiment_endpoint(request: SentimentRequest):
    text_lower = request.text.lower()
    if "good" in text_lower:
        return {"sentiment": "positive"}
    elif "bad" in text_lower:
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}
