# RHEL9

## How to build rhel image

```bash
export USER=ansible
docker build --build-arg RHEL_USER=$USER -t rhel-server .
```

## How to run rhel container

```bash
docker run -it -d --net ansible-net -h rhel --name rhel-server --cap-add SYS_ADMIN -v /sys/fs/cgroup:/sys/fs/cgroup --cgroupns=host rhel-server
```

## How to add ansible's public key

```bash
docker exec -t rhel-server sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to login into rhel container

```bash
docker exec -it -u $USER -w /home/$USER  rhel-server bash
```
