FROM node:16.10.0-alpine

WORKDIR /app

COPY package.json ./

COPY package-lock.json ./

COPY . .

EXPOSE 5173

RUN npm i

CMD ["npm", "run", "start"]

