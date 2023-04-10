#!/bin/sh

/usr/sbin/sshd -D -e &
/entrypoint.sh "$@"