from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class KeywordsRequest(BaseModel):
    text: str

@router.post("/keywords")
def keywords_endpoint(request: KeywordsRequest):
    words = request.text.split()
    unique_words = sorted(list(set(words)))
    return {"keywords": unique_words}