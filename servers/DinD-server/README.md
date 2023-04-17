# Docker in Docker

## How to build Docker in Docker image

```bash
export USER=ansible
docker build --build-arg DIND_USER=$USER -t dind-server .
```

## How to run Docker in Docker container

```bash
docker run --privileged -d --name dind-server -h dind --net ansible-net -p 9900-9999:9900-9999 dind-server
```

## How to add ansible's public key

```bash
docker exec -t dind-server sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to login into Docker in Docker container

```bash
docker exec -it -u $USER -w /home/$USER dind-server ash
```

## Reference links

https://github.com/docker-library/docker
https://github.com/jpetazzo/dind
