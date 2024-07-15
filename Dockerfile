FROM python:3.12-slim

ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

RUN poetry install --without dev

EXPOSE 5000

ENTRYPOINT ["poetry", "run", "python", "main.py"]
