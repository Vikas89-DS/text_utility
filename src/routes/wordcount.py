from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class WordCountRequest(BaseModel):
    text: str

@router.post("/wordcount")
def wordcount_endpoint(request: WordCountRequest):
    words = request.text.split()
    return {"wordcount": len(words)}
