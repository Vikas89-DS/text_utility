from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/summary")
async def summary_endpoint(request: TextRequest):
    summary = request.text.strip()
    if len(summary) > 120:
        summary = summary[:120] + "..."
    return {"summary": summary}
