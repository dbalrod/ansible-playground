# debian-server

## How to build debian-server image

```bash
export USER=ansible
docker build --build-arg DEBIAN_USER=$USER -t debian-server .
```

## How to run debian server

```bash
docker run -it -d --net ansible-net -h debian --name debian-server debian-server
```

## How to add ansible's public key

```bash
docker exec -t debian-server sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to log into ubuntu-server

```bash
docker exec -it -u $USER -w /home/$USER debian-server bash
```
