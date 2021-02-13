#!/bin/bash

git add .

read -p "Enter commmit message: " msg
git commit -m "$msg" 1 > /dev/null
echo -e "\033[32mcommitted the message '$msg'\033[0m"

echo "Pushing...."
git push &1 > /dev/null

echo -e "\033[32mPushed!\033[0m"
