from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Text Utility API is working"}

@app.post("/summary")
def summary_endpoint(text: str):
    # temporary placeholder logic
    return {"summary": text[:50]}
