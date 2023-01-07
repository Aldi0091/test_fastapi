FROM python:3.10-slim-buster
WORKDIR /application
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .