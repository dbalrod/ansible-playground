#!/bin/sh

/usr/sbin/sshd -D -e &
ln -s /run/postgresql/.s.PGSQL.5432 /tmp/.s.PGSQL.5432
docker-entrypoint.sh "$@"