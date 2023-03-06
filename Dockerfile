FROM --platform=$BUILDPLATFORM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

EXPOSE 8000

WORKDIR /drf_pytest_swagger

COPY . /drf_pytest_swagger

RUN pip install -U pip &&\
    pip install -r requirements.txt

