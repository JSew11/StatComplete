# syntax=docker/dockerfile:1
FROM node:12.2.0-alpine
WORKDIR /code/frontend
COPY package.json /code/frontend
COPY package-lock.json /code/frontend
RUN npm install
COPY . /code/frontend/