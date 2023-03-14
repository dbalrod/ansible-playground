# Mongo

## How to build Mongo image

```bash
export USER=ansible
docker build --build-arg MONGO_USER=$USER -t mongo .
```

## How to run Mongo

```bash
docker run --name mongo-db -h mongo --network ansible-net -d mongo
```

## How to add Mongo's public key

```bash
docker exec -t mongo-db bash -c "mkdir -p /home/$USER/.ssh && echo $(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub) >  /home/$USER/.ssh/authorized_keys"
```

## How to login into Mongo container

```bash
docker exec -it -u $USER mongo-db bash
```

## Reference links

https://hub.docker.com/_/mongo