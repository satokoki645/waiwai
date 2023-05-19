FROM python:3.12.0a7-alpine3.17

RUN apk add curl \
    && apk add git \
    && pip install --upgrade pip \
    && pip install fastapi uvicorn

WORKDIR /usr/src/python/api