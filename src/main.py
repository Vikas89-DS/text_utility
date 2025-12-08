from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Text Utility API is working"}

@app.post("/summary")
def summary_endpoint(text: str):
    # temporary placeholder logic
    return {"summary": text[:50]}

@app.post("/sentiment")
def sentiment_endpoint(text: str):
    # temporary placeholder logic
    text_lower = text.lower()
    if "good" in text_lower:
        return {"sentiment": "positive"}
    elif "bad" in text_lower:
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}

@app.post("/wordcount")
def wordcount_endpoint(text: str):
    words = text.split()
    return {"wordcount": len(words)}

