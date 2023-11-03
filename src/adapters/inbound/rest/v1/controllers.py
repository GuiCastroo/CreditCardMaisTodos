from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from http import HTTPStatus
from fastapi_pagination import Page
from src.adapters.outbound.repositories.credit_card_repository import CreditCardRepository
from src.domain.use_cases.create_new_creditcard_use_case import (
    CreateNewCreditCardDTOIn, CreateNewCreditCardDTOOut, CreateNewCreditCardUseCase
)
from src.domain.use_cases.get_one_credit_card_use_case import GetOneCreditCardUseCase
from src.domain.use_cases.get_all_credit_card_use_case import GetAllCreditCardUseCase
from src.adapters.inbound.rest.v1.dependencies import get_credit_card_repository
from pydantic import ValidationError
from creditcard.exceptions import BrandNotFound

credit_card_route = APIRouter(
    prefix='/credit-card',
    tags=["Credit Card"],
)


@credit_card_route.get(
    "/{identification}",
    status_code=HTTPStatus.OK,
    description="Get only credit card, filter by id that generation in created"
)
async def get_one_credit_card(
        identification,
        repo: CreditCardRepository = Depends(get_credit_card_repository)
) -> CreateNewCreditCardDTOOut:
    result = await GetOneCreditCardUseCase(repo).get(identification)
    if result:
        return result
    print(result)
    raise HTTPException(status_code=HTTPStatus.NO_CONTENT, detail=jsonable_encoder({'message': "Not found this id"}))


@credit_card_route.get("/", description="Get all credit card")
async def get_all_credit_card(
        repo: CreditCardRepository = Depends(get_credit_card_repository)
) -> Page[CreateNewCreditCardDTOOut]:
    result = await GetAllCreditCardUseCase(repo).get_all()
    return result


@credit_card_route.post("/", status_code=HTTPStatus.CREATED, description="Created a new credit card")
async def create_credit_card(
        body: CreateNewCreditCardDTOIn,
        repo: CreditCardRepository = Depends(get_credit_card_repository)
) -> CreateNewCreditCardDTOOut:
    try:
        result = await CreateNewCreditCardUseCase(repo).create(body)
        return result
    except ValidationError as error:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=jsonable_encoder(error.errors()))
    except BrandNotFound:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail={'error': "Not found brand the credit card"})
