#!/bin/bash

R="\033[91m"
G="\033[92m"
E="\033[0m"

#### NVIM ####
if [[ ! -d "~/.local/share/nvim/site/pack/packer" ]]; then
    echo "Deleting old packer directory..."
    rm -rf ~/.local/share/nvim/site/pack/packer
fi

printf "${G}Installing packer...${E}\n"
sleep 1
git clone --depth 1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim 2>/dev/null
mkdir -p ~/.config/nvim
printf "${G}Cloning repo...${E}\n"
sleep 2
git clone --depth 1 https://github.com/tamton-aquib/nvim.git ~/.config/nvim 2>/dev/null
nvim +PackerSync
