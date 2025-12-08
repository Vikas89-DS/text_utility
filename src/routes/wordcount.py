from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/wordcount")
async def wordcount_endpoint(request: TextRequest):
    return {"wordcount": len(request.text.split())}