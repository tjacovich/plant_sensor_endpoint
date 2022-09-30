FROM arm64v8/python:3.8

WORKDIR /app

COPY requirements.txt /app
COPY dev-requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
