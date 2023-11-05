import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.adapters.inbound.rest.v1.credit_card_controllers import credit_card_route
from src.adapters.inbound.rest.v1.user_controllers import authentic_router


def create_app():
    app = FastAPI(prefix="/v1")
    app.include_router(credit_card_route)
    app.include_router(authentic_router)
    add_pagination(app)

    @app.get('/health-check')
    def health_check():
        return {'message': 'ok'}

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(app)

