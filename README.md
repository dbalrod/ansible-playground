# ansible-playground

Ansible Docker container and multiple linux containers to run Ansible playbooks and roles inside them.

## Introduction

This repository includes:

1. An Ansible Docker Container and multiple playbooks and roles in `ansible` folder.

2. Multiple linux Docker containers in which can be run playbooks and roles. These containers can be found in `servers` folder.

3. Ansible AWX in `awx` folder. It provides a web-based user interface, REST API, and task engine built on top of Ansible.

## Getting started

There are 2 ways to use this Ansible playground:

1. Building and running Ansible Docker container and several linux Docker containers individually.

    > Take a look to the README file inside server folder to know how to build and run each container.

2. Using docker-compose to build and run Ansible Docker container and all linux Docker containers at once.

You can use docker-compose to build and run the full playground stack.

### How to build Ansible Docker container and linux Docker containers (servers)

```bash
docker-compose build
```

### How to start Ansible Docker container and linux Docker containers (servers)

```bash
docker-compose up -d
```

It is necessary to add Ansible Docker container's public key to servers' authorized_keys file:

```bash
for container in `docker-compose ps | awk '{print$1}' | sed -e '1,2d' | grep -vE "^ansible$"`
do
echo "Copying ansible container's pub key into $container's authorized_keys" 
docker exec -t $container sh -c "mkdir -p /home/ansible/.ssh && echo '$(docker exec -t ansible cat /home/ansible/.ssh/ssh_host_ed25519_key.pub)' > /home/ansible/.ssh/authorized_keys" 
done
```

### How to build and run AWX

AWX brings its own `docker-compose.yml` file inside its folder. There is also a README file with the instructions about how to run AWX.