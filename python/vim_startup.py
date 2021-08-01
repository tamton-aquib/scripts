#!/usr/bin/env python3
import subprocess as sub
import os
import re
# NOTE: This is not working quite as expected as the `-q` just after startup behaves differently.

def check_vimlog():
	if 'vim.log' in os.listdir('.'):
		sub.run('rm vim.log'.split())

def prettify_result(time, plugs_total):
	nice = "\033[31m" if time > 200 else "\033[32m"
	END = "\033[0m"
	print("=========================")
	print(f"{nice}{str(round(time, 2)).center(23)}{END}")
	print("=========================")
	print(plugs_total)

def get_file_contents():
	lines = [line for line in open('vim.log', 'r').read().split('\n') if line and 'clock' not in line]
	sorted_list = sorted(lines, key = lambda x: x.split()[1], reverse=True)[:40]
	total_time = 0
	plugs_total = ""

	for item in sorted_list:
		item_time = item.split()[1]
		item_name = "".join(item.split()[2:])
		try:
			item_time = float(item_time[:-1]) if item_time.endswith(':') else float(item_time)
			total_time += item_time
		except: continue
		if 'packer' in item_name:
			plug_name = re.findall(r"packer/start/(.+?)/.+?/", item_name)
			plug_name = plug_name[0] if plug_name else "packer_compiled.vim"
			plugs_total += f"{str(item_time).ljust(8)} : {plug_name}\n"

	prettify_result(total_time, plugs_total)

if __name__ == '__main__':
	check_vimlog()
	sub.run(['nvim', '--startuptime', 'vim.log', '-f', '-c', 'q'])
	get_file_contents()
	check_vimlog()

