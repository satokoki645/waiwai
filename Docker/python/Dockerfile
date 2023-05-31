FROM python:3.11.3-alpine3.18

RUN apk add curl \
    && apk add git \
    && pip install --upgrade pip \
    && pip install fastapi uvicorn

WORKDIR /usr/src/python/api