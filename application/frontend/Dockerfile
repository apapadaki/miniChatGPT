# Build Remix app artifacts
FROM node:16-alpine as build
WORKDIR /app
COPY ./package.json ./
RUN npm install
COPY ./ .
RUN npm run build

# Deploy artifacts to container
FROM node:16-alpine
WORKDIR /app
COPY ./package.json ./
RUN npm install --omit=dev
COPY --from=build /app/build /app/build
ENV NODE_ENV=production
CMD npm run start