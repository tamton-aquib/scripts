#!/usr/bin/bash
# echo "Private:  $(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')"
NOICE=$(ifconfig | grep "broadcast" | awk '{print $2}')
echo "Private:  $NOICE"

echo "Public :  $(curl -s ifconfig.me)"
