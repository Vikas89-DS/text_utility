from fastapi import APIRouter

router = APIRouter()

@router.post("/keywords")
def keywords_endpoint(text: str):
    words = text.split()
    unique_words = list(set(words))
    return {"keywords": unique_words}
