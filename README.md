# Some scripts I use.

### Get a minimal virmc:

A oneliner to set up a minimal vimrc on ur machine (another way is to manually download install.sh and execute it)

```sh
curl -sL git.io/vim_install | bash
```
### Other scripts:

#### Bash

* `neofetch.sh`
	* Tweaked version of [NerdFetch](https://github.com/ThatOneCalculator/NerdFetch).
* `my_ip.sh`
	* for showing private and public ips.
* `wifi.sh` 
	* for connecting to wifi via command line.

#### Python
* `ctf.py` (❗ This was removed in favour of [ice](https://github.com/tamton-aquib/ice))
	* Has 2 functions (for now).
	* morse and rot(caesar).
	* Usage: `python3 ctf.py rot/morse "The_String"`
* `translate.py`
	* Translates other languages to english.
	* Converts the text in clipboard.
	* Automatically detects the language. (uses googletrans module)
* `vim_startup.py` (❗ Probably wont work anymore as this was from nvim 0.3)
	* To get nvim startuptime.
	* Along with plugin-timings.
	* looks for paq directory for profiling plugin startuptime.
* `colors.py` 
	* grabs the color where mouse is pointed to on the screen.
	* In hex and rgb.
	* Requirement: Tkinter.
* `unicode_arrows.py` 
	* prints some unicode arrow characters.
	* Sometimes i use it for terminal customization.
* `gh.py`
    * github related commands.
    * `issues/pr`, `follow`
