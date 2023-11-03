from fastapi import FastAPI
import uvicorn


def create_app():
    app = FastAPI()

    @app.get('/health-check')
    def health_check():
        return {'message': 'ok'}

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(app)

