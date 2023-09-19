FROM node:latest

ENV NODE_ENV production
ENV LISTEN_PORT=3003

WORKDIR /app
COPY ./app .
CMD [ "node", "app.js" ]