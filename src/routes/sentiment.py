from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/sentiment")
async def sentiment_endpoint(request: TextRequest):
    txt = request.text.lower()
    if "good" in txt or "great" in txt or "love" in txt or "best" in txt:
        return {"sentiment": "positive"}
    elif "bad" in txt or "worst" in txt or "hate" in txt or "terrible" in txt:
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}