from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.adapters.inbound.rest.v1.dependencies import get_user_repository, get_current_active_user
from src.adapters.inbound.rest.v1.token_jwt import (
    User,
    UserCreate,
    verify_password,
    create_jwt_token,
    pwd_context,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    timedelta,
    Token
)
from src.adapters.outbound.repositories.user_repository import UserRepository

authentic_router = APIRouter(
    prefix='/auth',
    tags=["JWT"],
)


@authentic_router.post("/create-user")
async def create_user(user: UserCreate, repo: UserRepository = Depends(get_user_repository)):
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    await repo.create(user)
    return user


@authentic_router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        repo: UserRepository = Depends(get_user_repository)
):
    user = await repo.get_by_filter(form_data.username)
    status = verify_password(form_data.password, user.password)
    print(status)
    if not user or not status:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@authentic_router.get("/users/me/", response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@authentic_router.get("/users/me/items/")
async def read_own_items(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]
