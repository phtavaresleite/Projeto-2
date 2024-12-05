FROM python:3.9-alpine3.13

COPY ./requirements.txt /tmp/requirements.txt
COPY ./django2 /django2
WORKDIR /django2
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client &&\
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/* && \
    apk del .tmp-build-deps && \
    adduser \
    -D \
    -H \
    django-user /bin/sh

ENV PATH='/py/bin:$PATH'

USER django-user