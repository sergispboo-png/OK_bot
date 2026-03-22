from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "server running"}

@app.post("/webhook")
async def webhook(data: dict):
    print("Пришло:", data)
    return {"ok": True}
