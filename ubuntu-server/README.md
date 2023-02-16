# ubuntu-server

## How to build ubuntu-server image

```bash
docker build --build-arg UBUNTU_USER=ansible -t ubuntu-server .
```

## How to run ubuntu-server

```bash
docker run -it -d --net ansible-net -h ubuntu --name ubuntu-server ubuntu-server
docker exec -t ubuntu-server sh -c "mkdir -p /home/ansible/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/ansible/.ssh/authorized_keys"
docker exec -it -u ansible -w /home/ansible ubuntu-server bash
```
