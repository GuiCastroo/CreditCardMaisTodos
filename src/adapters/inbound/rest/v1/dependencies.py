from http import HTTPStatus
from typing import Annotated

from fastapi import Depends
from fastapi.exceptions import HTTPException
from jose import JWTError

from src.adapters.inbound.rest.v1.token_jwt import (
    User,
    oauth2_scheme,
    jwt,
    SECRET_KEY,
    ALGORITHM,
    TokenData
)
from src.adapters.outbound.orm.database import AsyncSession, get_db
from src.adapters.outbound.repositories.credit_card_repository import CreditCardRepository
from src.adapters.outbound.repositories.user_repository import UserRepository


async def get_credit_card_repository(db: AsyncSession = Depends(get_db)):
    return CreditCardRepository(db)


async def get_user_repository(db: AsyncSession = Depends(get_db)):
    return UserRepository(db)


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        repo: UserRepository = Depends(get_user_repository)
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.FORBIDDEN,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = repo.get_by_filter(value=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
):
    user = await current_user
    if not user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user
