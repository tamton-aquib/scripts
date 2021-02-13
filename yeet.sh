#!/bin/bash

git add . # Yeah adding current directory is not optimal, ik.

read -p "Enter commmit message: " msg
git commit -m "$msg"
echo -e "\033[32mcommitted with message '$msg'\033[0m"

echo "Pushing...."
git push

echo -e "\033[32mPushed!\033[0m"
