FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

# Copy the rest of the application code
COPY . /app/
