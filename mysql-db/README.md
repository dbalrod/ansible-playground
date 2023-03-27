# Mysql

## How to build Mysql image

```bash
export USER=ansible
docker build --build-arg MYSQL_USER=$USER -t mysql .
```
## How to run Mysql

```bash
docker run --name mysql-db --network ansible-net -h mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql
```
## How to add Mysql's public key

```bash
docker exec -t mysql-db bash -c "mkdir /home/$USER/.ssh && echo $(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub) >  /home/$USER/.ssh/authorized_keys"
```

## How to login into Mysql container

```bash
docker exec -it -u $USER mysql-db bash
```

## Reference links

https://stackoverflow.com/questions/63791797/why-can-ansible-not-connect-to-mysql
https://dba.stackexchange.com/questions/102066/ansible-how-to-change-mysql-server-root-password-by-reprovisioning-the-server