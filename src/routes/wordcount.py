from fastapi import APIRouter

router = APIRouter()

@router.post("/wordcount")
def wordcount_endpoint(text: str):
    words = text.split()
    return {"wordcount": len(words)}
