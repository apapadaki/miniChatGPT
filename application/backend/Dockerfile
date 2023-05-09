# Build stage where the environment is created and extracted
# to a standalone env that can be used on any system.
# This allows for a minimal base image to be used for the
# deployed env which will result in a small Docker image overall,
# that holds only the essential dependencies for the app.
FROM continuumio/miniconda3:latest as builder

WORKDIR /home/docker_conda_template

# Create environment
COPY environment.yml ./

RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "backend", "/bin/bash", "-c"]

# Install gunicorn server to use instead of default flask server
RUN conda install -c conda-forge gunicorn

# Use conda-pack to create a standalone enviornment
RUN conda install -c conda-forge conda-pack
RUN conda-pack -n backend -o /tmp/env.tar && \
  mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
  rm /tmp/env.tar

RUN /venv/bin/conda-unpack

FROM debian:buster

# Get application source code
COPY src ./src
COPY app.py ./

# Get environment from build phase
COPY --from=builder /venv /venv

# Enable the environment and start the app
SHELL ["/bin/bash", "-c"]
EXPOSE 5000
ENTRYPOINT source /venv/bin/activate && \
           gunicorn -b 0.0.0.0:5000 app:app

