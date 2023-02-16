# alpine-server

## How to build alpine-server image

```bash
docker build --build-arg ALPINE_USER=alpine -t alpine-server .
```

## How to run alpine-server

```bash
docker run -it -d --net ansible-net -h alpine --name alpine-server alpine-server
docker exec -t alpine-server sh -c "mkdir -p /home/alpine/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/alpine/.ssh/authorized_keys"
docker exec -it -u alpine -w /home/alpine alpine-server ash
```
