# Rockylinux

## How to build rockylinux image

```bash
export USER=ansible
docker build --build-arg ROCKY_USER=$USER -t rockylinux-server .
```

## How to run rockylinux container

```bash
docker run -it -d --net ansible-net -h rockylinux --name rockylinux-server --cap-add SYS_ADMIN -v /sys/fs/cgroup:/sys/fs/cgroup --cgroupns=host rockylinux-server
```

## How to add ansible's public key

```bash
docker exec -t rockylinux-server sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to log into centos container

```bash
docker exec -it -u $USER -w /home/$USER rockylinux-server bash
```
