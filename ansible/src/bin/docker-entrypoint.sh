#!/bin/sh
sudo postfix -v start-fg &
exec "$@"