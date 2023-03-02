# CENTOS7

## How to build centos image

```bash
export USER=ansible
docker build --build-arg CENTOS_USER=$USER -t centos-server .
```

## How to run centos container

```bash
docker run -it -d --net ansible-net -h centos --name centos-server --cap-add SYS_ADMIN -v /sys/fs/cgroup:/sys/fs/cgroup --cgroupns=host centos-server
```

## How to add ansible's public key

```bash
docker exec -t centos-server sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to login into centos container

```bash
docker exec -it -u $USER -w /home/$USER centos-server bash
```
