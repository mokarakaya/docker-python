# hub
the repository for a sample docker image to run python code

# Steps

## Login (if you have not)
- create an access token in https://hub.docker.com/settings/security
- `docker login --username <username>`
- use access token as password

# Build and push
- `cd hub`
- `docker build -t <username>/docker-python:0.1 .`
- `docker run <username>/docker-python:0.1`
- `docker push <username>/docker-python:0.1`
- check your image available at `https://hub.docker.com/repository/docker/<username>/docker-python`

# Autobuild
- Autobuild in docker will build/update the image with tag `latest` when there are new commits in master.
- `https://hub.docker.com/repository/docker/<username>/docker-python/builds`
- See an example here: `https://hub.docker.com/repository/docker/mokarakaya/docker-python/builds`
