# pull official base image
FROM node:18-alpine

# set working directory
WORKDIR /usr/src/eventfrontend

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/eventfrontend/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm ci
RUN npm install react-scripts@5.0.1 -g --silent

# start app
CMD ["npm", "start"]