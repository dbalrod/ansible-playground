# Ansible

## How to build the ansible image

```bash
docker build -t ansible --build-arg ANSIBLE_USER=ansible .
```

where ANSIBLE_USER is the name of the user that will run ansible.

## Create ansible network for ansible and other servers

```bash
docker network create ansible-net
```

## How to run ansible container

```bash
docker run -t -d --net ansible-net -h ansible -v $PWD/ansible-examples:/etc/ansible -w /etc/ansible --name ansible ansible
```

## Test that ansible is correctly installed

```bash
docker exec -it ansible ash
/etc/ansible $ ansible --version
ansible [core 2.14.2]
  config file = None
  configured module search path = ['/home/ansible/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/ansible/.local/lib/python3.10/site-packages/ansible
  ansible collection location = /home/ansible/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/ansible/.local/bin/ansible
  python version = 3.10.10 (main, Feb  9 2023, 02:08:14) [GCC 12.2.1 20220924] (/usr/bin/python3)
  jinja version = 3.1.2
  libyaml = False
```

## Run ansible examples

1. Copy files to servers

```ash
/etc/ansible $ ansible-playbook playbooks/copy_hosts_nsswitch.yml
```