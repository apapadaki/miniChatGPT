# miniChatGPT Flask Backend

RestAPI and Websocket built with Flask, Flask-RESTful for the API and Flask-SocketIO for the Websockets.
The RestAPI is responsible to serve conversation information while the Websockets are responsible to handle the conversation itself.

- [Flask Docs](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask-RESTful Docs](https://flask-restful.readthedocs.io/en/latest/index.html)
- [Flask-SocketIO Docs](https://flask-socketio.readthedocs.io/en/latest/index.html)

## Requirements

- Anaconda

## Getting started

The following commands should be executed in a terminal in the /backend directory.

- Create a virtual environment:

```sh
conda env create -f environment.yml
```

- Activate the new environment:

```sh
conda activate backend
```

- Start the Flask server:

```sh
flask --debug run
```

- To deactivate the environemnt run:

```sh
conda deactivate
```

## Deployment (Docker)

Run the following commands from your terminal in the /backend directory.

Build docker image:

```sh
docker build . -t minichatgpt/backend
```

Create and start the container:

```sh
docker run -p 5000:5000 minichatgpt/backend
```

[Click here](http://localhost:5000/api/conversations) to see the default api endpoint.
