from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SummaryRequest(BaseModel):
    text: str

@router.post("/summary")
def summary_endpoint(request: SummaryRequest):
    text = request.text
    return {"summary": text[:50]}
