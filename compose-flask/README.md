# compose-flask

- Here we configure a docker-compose file which has two services, namely `flask-server`, and `flask-client`
- `flask-client` calls `flask-server` by using the container name and the internal port. (`flask-server:5000`)

# Steps

- `docker-compose up`
- `curl http://localhost:5003/flaskclient`