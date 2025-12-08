from fastapi import FastAPI
from routes.summary import router as summary_router
from routes.sentiment import router as sentiment_router
from routes.wordcount import router as wordcount_router
from routes.keywords import router as keywords_router



app = FastAPI()

app.include_router(summary_router)
app.include_router(sentiment_router)
app.include_router(wordcount_router) 
app.include_router(keywords_router)

@app.get("/")
def root():
    return {"message": "Text Utility API is working"}