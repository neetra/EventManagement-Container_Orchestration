# pull official base image
FROM node:18-alpine

# set working directory
WORKDIR /frontend



# install and cache app dependencies
COPY package.json /frontend/package.json
COPY package-lock.json /frontend/package-lock.json
RUN npm i
RUN npm install react-scripts@5.0.1 -g --silent
COPY . /frontend
# start app
CMD ["npm", "start"]