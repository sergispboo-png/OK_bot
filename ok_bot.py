from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/ok/webhook")
async def ok_webhook(request: Request):

    data = await request.json()

    print("OK EVENT RECEIVED:")
    print(data)

    return {"status": "ok"}
