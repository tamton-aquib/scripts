#!/bin/fish

nmcli radio wifi on
sleep 1
set wifi_name (nmcli device wifi list | tail -n +2 | fzf)
set SSID (echo "$wifi_name" | grep -oP "([A-F0-9]{2}:){5}[A-F0-9]{2}")

nmcli device wifi connect --ask $SSID
