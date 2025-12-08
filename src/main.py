from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Text Utility API is working"}
