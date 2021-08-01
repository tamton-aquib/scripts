#!/bin/bash

R="\033[91m"
G="\033[92m"
E="\033[0m"

read -p "Which vim are you using? [vim/nvim]: " VIM_VERSION
read -p ""

#### VIM ####
if [[ "$VIM_VERSION" == "vim" ]] then
	curl -s -Lo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
	curl -s "https://raw.githubusercontent.com/tamton-aquib/dotfiles/main/.vimrc" > ~/.vimrc
	vim -c ":PlugInstall"
	echo "colorscheme onedark" >> ~/.vimrc

#### NVIM ####
elif [[ "$VIM_VERSION" == "nvim" ]] then
	read -p "VimL config or lua [viml/lua]: " VIM_OR_LUA
	if [[ "$VIM_OR_LUA" == "vim" ]] then
		curl -s -Lo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
		mkdir -p ~/.config/nvim
		curl -s "https://raw.githubusercontent.com/tamton-aquib/dotfiles/main/.vimrc" > ~/.config/nvim/init.vim
		nvim -c "echo 'Installing Plugins (Usually takes around 30s.)' | :PlugInstall"
		echo "colorscheme onedark" >> ~/.config/nvim/init.vim
	else
		curl -sL git.io/tajvim | bash
	fi

else
	echo -e "${R}Enter valid vim version.${E}"
fi
