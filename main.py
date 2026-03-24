from fastapi import FastAPI, Request
import requests

app = FastAPI()

ACCESS_TOKEN = "-n-UZ0QnFdojl9EccizTKQYOVp6JpDTpzlGt7u2MvXuUz4qDOBL784Ca4Dh3RTIzbWbPABdgDAzLCk7kiWN1"

@app.get("/")
def home():
    return {"status": "server running"}


@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    print(data)

    # Проверяем, есть ли сообщение
    if "message" in data:
        user_id = data["message"]["from"]["user_id"]
        text = data["message"]["text"]

        send_message(user_id, f"Ты написал: {text}")

    return {"ok": True}


def send_message(user_id, text):
    url = "https://api.ok.ru/fb.do"
    params = {
        "method": "messages.send",
        "access_token": ACCESS_TOKEN,
        "user_id": user_id,
        "message": text,
        "format": "json"
    }
    requests.post(url, params=params)
