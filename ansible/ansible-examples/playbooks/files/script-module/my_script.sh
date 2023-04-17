#!/bin/sh
echo "This is start of my script!"
touch /tmp/foo
ls -lrt /tmp/foo
rm -rf /tmp/foo
echo "This is  end  of my script!"