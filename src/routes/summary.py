from fastapi import APIRouter

router = APIRouter()

@router.post("/summary")
def summary_endpoint(text: str):
    return {"summary": text[:50]}
