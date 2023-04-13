# alpine-server

## How to build alpine-server image

```bash
export USER=ansible
docker build --build-arg ALPINE_USER=$USER -t alpine-server .
```

## How to run alpine-server

```bash
docker run -it -d --net ansible-net --cap-add NET_ADMIN --cap-add SYS_ADMIN -h alpine --name alpine-server alpine-server
```

## How to add ansible's public key

```bash
docker exec -t alpine-server sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to login into alpine-server container

```bash
docker exec -it -u $USER -w /home/$USER alpine-server ash
```
