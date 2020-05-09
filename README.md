# docker-python
the repository for a sample docker image to run python code



# Steps

## Login (if you have not)
- create an access token in https://hub.docker.com/settings/security
- `docker login --username <username>`
- use access token as password

# Build and push
- `cd docker-python`
- `docker build -t <username>/docker-python:0.1 .`
- `docker run <username>/docker-python:0.1`
- `docker push <username>/docker-python:0.1`
- check your image available at `https://hub.docker.com/repository/docker/<username>/docker-python`
