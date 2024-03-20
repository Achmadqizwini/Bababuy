from fastapi import APIRouter

router = APIRouter()

fake_user_db = {"animal": "beluga", "gender": "male"}


@router.get("/users/", tags=["users"])
async def read_users():
    return fake_user_db

@router.get("/users/me", tags=["users"])
async def read_users_me():
    return {"username" : "Achmad Qizwini"}

@router.get("users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}