# syntax=docker/dockerfile:1
FROM tarampampam/node:19-alpine
WORKDIR /code/client
COPY package.json /code/client
COPY package-lock.json /code/client
RUN npm install
COPY . /code/client/