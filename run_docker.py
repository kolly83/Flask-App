#!/usr/bin/env bash

# Build image
docker build -t my-python-app .

# List docker images
docker image ls

# Run flask app
docker run -p 8000:5000 my-running-app
