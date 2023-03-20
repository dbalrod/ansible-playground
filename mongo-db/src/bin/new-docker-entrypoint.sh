#!/bin/bash

/usr/sbin/sshd -D -e &
docker-entrypoint.sh "$@"