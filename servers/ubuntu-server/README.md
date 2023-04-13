# ubuntu-server

## How to build ubuntu-server image

```bash
export USER=ansible
docker build --build-arg UBUNTU_USER=$USER -t ubuntu-server .
```

## How to run ubuntu-server

```bash
docker run -it -d --net ansible-net -h ubuntu --name ubuntu-server ubuntu-server
```

## How to add ansible's public key

```bash
docker exec -t ubuntu-server sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to log into ubuntu-server

```bash
docker exec -it -u $USER -w /home/$USER ubuntu-server bash
```
