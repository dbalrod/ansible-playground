# InfluxDB

## How to build InfluxDB image

```bash
export USER=ansible
docker build --build-arg INFLUXDB_USER=$USER -t influxdb .
```

## How to run InfluxDB

```bash
docker run -d -p 8086:8086 -v $PWD/data:/var/lib/influxdb2 -v $PWD/config:/etc/influxdb2 -e DOCKER_INFLUXDB_INIT_MODE=setup -e DOCKER_INFLUXDB_INIT_USERNAME=my-user -e DOCKER_INFLUXDB_INIT_PASSWORD=my-password -e DOCKER_INFLUXDB_INIT_ORG=my-org -e DOCKER_INFLUXDB_INIT_BUCKET=my-bucket -e DOCKER_INFLUXDB_INIT_RETENTION=1w -e DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=my-super-secret-auth-token --net ansible-net -h influxdb --name influxdb-db influxdb
```

## How to add InfluxDB's public key

```bash
docker exec -t influxdb-db sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to login into InfluxDB container

```bash
docker exec -it -u $USER influxdb-db ash
```

## Reference links

https://hub.docker.com/_/influxdb
http://localhost:8086