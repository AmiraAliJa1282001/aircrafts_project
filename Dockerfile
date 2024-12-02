FROM python:3.11.4-slim-buster

WORKDIR /D:/Django/Aircraft_project/aircraft_project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNPUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt 

COPY . .