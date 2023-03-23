# syntax=docker/dockerfile:1
FROM node:19.8.1-alpine
WORKDIR /code/client
COPY package.json /code/client
COPY package-lock.json /code/client
RUN npm install
COPY . /code/client/