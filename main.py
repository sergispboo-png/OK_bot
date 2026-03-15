from fastapi import FastAPI
from ok_bot import router as ok_router

app = FastAPI()

@app.get("/")
def home():
    return {"status": "server running"}

app.include_router(ok_router)
