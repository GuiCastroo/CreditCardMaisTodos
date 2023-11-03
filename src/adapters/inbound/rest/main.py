from fastapi import FastAPI
import uvicorn
from src.adapters.inbound.rest.v1.controllers import credit_card_route
from fastapi_pagination import add_pagination


def create_app():
    app = FastAPI(prefix="/v1")
    app.include_router(credit_card_route)
    add_pagination(app)

    @app.get('/health-check')
    def health_check():
        return {'message': 'ok'}

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(app)

