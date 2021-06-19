# Some scripts I use.

### Get my virmc:

To set up my vimrc on ur machine, do this one-liner (or you can manually download install.sh and execute it)

```sh
curl -sL git.io/vimconfig > install.sh && bash install.sh && rm install.sh
```
<details>
<summary>Current Plugins:</summary>
<ul>
<li> vim-closetag</li>
<li> vim-floaterm</li>
<li> onedark theme</li>
<li> fzf-vim</li>
<li> vim-polyglot</li>
<li> auto-pairs</li>
</ul>
</details>

### Other scripts:

* `neofetch.sh`
    * Tweaked version of [NerdFetch](https://github.com/ThatOneCalculator/NerdFetch).
* `translate.py`
    * Translates other languages to english.
    * Converts the text in clipboard.
    * Automatically detects the language. (uses googletrans module)
*	`vim_startup.py`
	* To get nvim startuptime.
	* Along with plugin-timings.
	* looks for paq directory for profiling plugin startuptime.
* `colors.py` 
    * grabs the color where mouse is pointed to on the screen.
    * In hex and rgb.
    * Requirement: Tkinter.
* `my_ip.sh`
	* for showing private and public ips.
* `unicode_arrows.py` 
    * prints some unicode arrow characters.
    * Sometimes i use it for terminal customization.
* `wifi.sh` for connecting to wifi via command line.
