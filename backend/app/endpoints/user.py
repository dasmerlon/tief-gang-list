from app import app

from uuid import UUID


@app.get("/user/{user_id}")
async def read_user(user_id: UUID):
    return {"user_id": user_id}