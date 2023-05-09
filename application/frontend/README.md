# miniChatGPT Remix Frontend

- [Remix Docs](https://remix.run/docs)

## Requirements

- [Node.js](https://nodejs.org/en/download/) >=16.0.0
- npm 7 or greater

## Development

From your terminal in the /frontend directory:

- Install packages

```sh
npm install
```

- Start the web server in dev mode

```sh
npm run dev
```

This starts your app in development mode, rebuilding assets on file changes.
[Click here](http://localhost:3000) to be navigated to the app.

## Deployment (Docker)

Run the following commands from your terminal in the /frontend directory.

Build docker image:

```sh
docker build . -t minichatgpt/frontend
```

Create and start the container:

```sh
docker run -p 3000:3000 minichatgpt/frontend
```

[Click here](http://localhost:3000) to be navigated to the app.
