FROM python:3.8

WORKDIR /usr/src/pipelines

RUN apt-get update && apt-get upgrade && pip install websocket-client

COPY . .
EXPOSE 80

CMD [ "pwd", "ls"]