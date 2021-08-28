FROM node:16.8.0

WORKDIR /frontend

COPY package.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]