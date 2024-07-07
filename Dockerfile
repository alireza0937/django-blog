FROM python:3.10.14-slim-bullseye
ENV PYTHONUNBUFFERD 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY ./req.txt .
RUN pip install --upgrade pip \
    && pip install -r req.txt
COPY . /app
