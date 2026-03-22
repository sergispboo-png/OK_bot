from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "OK bot running"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("EVENT FROM OK:", data)
    return {"status": "ok"}
