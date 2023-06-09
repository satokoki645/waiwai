FROM --platform=linux/x86_64 python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add curl && \
    apk add git

RUN pip install poetry && \
    poetry config virtualenvs.create false

RUN poetry init

RUN /bin/sh -c poetry add fastapi uvicorn sqlalchemy alembic && \
    /bin/sh -c poetry install

WORKDIR /usr/src/python/api

RUN echo 'python container run'