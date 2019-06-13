FROM python:3.8.0b1-alpine

WORKDIR /usr/src/app

# RUN apk add ipython
# RUN pip install ipython

COPY . .
