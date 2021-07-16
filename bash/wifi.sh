#!/usr/bin/bash

nmcli radio wifi on
sleep 1
wifi_name=$(nmcli device wifi list | tail -n +2 | fzf)
SSID=$(echo "$wifi_name" | grep -oP "([A-F0-9]{2}:){5}[A-F0-9]{2}")

nmcli device wifi connect --ask $SSID
