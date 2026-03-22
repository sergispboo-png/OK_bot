from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK bot running"}

@app.post("/webhook")
async def webhook(data: dict):
    print(data)
    return {"ok": True}
