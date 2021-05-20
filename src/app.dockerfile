FROM python:3.9.4-alpine

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev bash \
    && pip install --upgrade pip setuptools wheel

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt