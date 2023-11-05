# Use the base Python image
FROM python:3.10-slim-buster

# Set environment variables

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry env use 3.10.9 && poetry install --no-dev

COPY . /app/

EXPOSE 8000

RUN poetry run alembic upgrade head

CMD ["poetry", "run", "uvicorn", "src.adapters.inbound.rest.main:app", "--host", "0.0.0.0", "--port", "8000"]
