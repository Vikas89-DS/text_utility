from fastapi import FastAPI
from routes.keywords import router as keywords_router
from routes.wordcount import router as wordcount_router
from routes.sentiment import router as sentiment_router
from routes.summary import router as summary_router

app = FastAPI(title="Text Utility API")

app.include_router(keywords_router, tags=["keywords"])
app.include_router(wordcount_router, tags=["wordcount"])
app.include_router(sentiment_router, tags=["sentiment"])
app.include_router(summary_router, tags=["summary"])

@app.get("/")
def root():
    return {"message": "Text Utility API is working"}