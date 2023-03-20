# AWX

## How to deploy AWX

1. Run postgres database and wait until database is ready

    ```bash
    docker-compose up -d postgres
    while ! docker-compose exec postgres pg_isready; do sleep 1; echo "Waiting for postgres db to start"; done
    ```

2. Populate database

    ```bash
    docker-compose run --rm --service-ports task awx-manage migrate --no-input
    ```

3. Start AWX and create preloaded data

    ```bash
    docker-compose up -d
    docker exec awx_web '/usr/bin/update-ca-trust'
    docker exec awx_task '/usr/bin/update-ca-trust'
    docker exec awx_task bash -c "/usr/bin/awx-manage create_preload_data"
    ```

4. Create a ssh key to connect to servers

    ```bash
    docker-compose exec task ssh-keygen -t ed25519 -f /root/.ssh/ssh_host_ed25519_key -q -N ""
    ```

5. Add AWX ssh pub key to servers

    This example shows how to add AWX's ssh public key to a server named alpine-server with an user named ansible.

    ```bash
    docker exec -t alpine-server sh -c "mkdir -p /home/ansible/.ssh && echo '$(docker-compose exec task cat /root/.ssh/ ssh_host_ed25519_key.pub)' >> /home/ansible/.ssh/authorized_keys"
    ```

## How to configure AWX

It is necessary to create an inventory and indicate the user name and ssh key that will be used to connect to servers that will take part of this inventory.

```yaml
ansible_ssh_private_key_file: /root/.ssh/ssh_host_ed25519_key
ansible_user: ansible
```

## How to connect to AWX

AWX will be available at <http://localhost:8052>
