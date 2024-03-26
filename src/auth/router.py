from fastapi import APIRouter, Depends

from auth.schemas import User
from auth.repository import UserRepository
from auth.utils import create_jwt_token, get_username_from_token

router = APIRouter()

@router.post("/login")
async def login(user_in: User):

    user = UserRepository.get_user(user_in.username)

    if user:
        if user.password == user_in.password:
            return { "access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer" }

    return {"error": "Invalid credentials"}

@router.post("/register")
async def register(user_in: User):

    user = UserRepository.get_user(user_in.username)

    if user:
        return {"error": "This username is taken"}

    UserRepository.add_user(user_in)
    return { "access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer" }

@router.get("/about_me")
async def about_me(current_user: str = Depends(get_username_from_token)):
    user = UserRepository.get_user(current_user)
    if user:
        return user
    return {"error": "User not found"}



