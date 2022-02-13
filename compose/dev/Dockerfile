FROM python:3.8-slim-bullseye

WORKDIR /opt/app

COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN poetry install

COPY src/. .

WORKDIR /opt/app/src

CMD ["poetry", "run", "uvicorn", "main:app", "--port", "8000"]
