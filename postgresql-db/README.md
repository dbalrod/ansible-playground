# Postgresql

## How to build Postgresql image

```bash
export USER=ansible
docker build --build-arg PSQL_USER=$USER -t postgres .
```
## How to run Postgresql

```bash
docker run --name postgres-db -e POSTGRES_PASSWORD=my-secret-pw --network ansible-net -h postgres -d postgres
```
## How to add Postgresql's public key

```bash
docker exec -t postgres-db sh -c "mkdir -p /home/$USER/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/$USER/.ssh/authorized_keys"
```

## How to login into Postgresql container

```bash
docker exec -it -u $USER postgres-db ash
```

## Reference links

https://hub.docker.com/_/postgres
https://stackoverflow.com/questions/5500332/cant-connect-the-postgresql-with-psycopg2