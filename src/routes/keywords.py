from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/keywords")
async def keywords_endpoint(request: TextRequest):
    words = request.text.lower().split()
    unique = sorted(list(set(words)))
    return {"keywords": unique}