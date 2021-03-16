#!/bin/bash

# Below command is for swapping Esc and caps key (Works perfectly on ubuntu)
# setxkbmap -option caps:swapescape 

# COLORS

R="\033[91m"
G="\033[92m"
E="\033[0m"

echo
echo -e "${G}Welcome to configuring your vimrc${E}"
echo "--------------------------------"
echo

read -p "Which vim are you using? [vim/nvim]: " VIM_VERSION
echo

if [[ -z "$VIM_VERSION" ]]
then
  echo 'Usage: "./install.sh vim/nvim"'
  exit
fi


#### VIM ####
if [[ "$VIM_VERSION" == "vim" ]]
then
  echo -e "${G}You have selected vanilla vim.${E}"
  echo -e "Setting Up Plug manager for vim..."
  sleep 2 # For effect :)

  curl -s -Lo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  echo -e "${G}Setup complete.${E}"
  echo
  sleep 1
  echo "Downloading contents and settings from github....[18.5KB]"
  sleep 2
  curl -s "https://raw.githubusercontent.com/tamton-aquib/dotfiles/main/.vimrc" > ~/.vimrc
  echo -e "${G}Downloading complete.${E}"
  echo
  echo "Opening up vim and setting up plugins....."
  sleep 3
  vim -c ":PlugInstall"

#### NVIM ####
elif [[ "$VIM_VERSION" == "nvim" ]]
then
  echo -e "${G}You have selected neovim.${E}"
  sleep 1

  sh -c 'curl -s -Lo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  mkdir -p ~/.config/nvim
  echo
  echo "Downloading config file from github."
  sleep 3
  echo -e "${G}Downloaded 18.5kB.${E}"
  echo
  sleep 1
  echo "Setting up and configuring files..."
  sleep 3
  curl -s "https://raw.githubusercontent.com/tamton-aquib/dotfiles/main/.vimrc" > ~/.config/nvim/init.vim
  echo -e "${G}Setup complete.${E}"
  sleep 2

  echo
  echo -e "Opening neovim and setting up ${G}Plugins${E}"
  sleep 2

  nvim -c "echo 'Installing Plugins(Usually takes below 30s.)' | :PlugInstall"

  echo -e "${G}Setup Complete.${E}"




else
  echo -e "\033[91mEnter valid vim version. (Currently gvim not supported.)\033[0m"
fi
