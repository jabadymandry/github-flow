
:bulb: **Tip**: if you can see this tip your Github account is correctly linked, you can go on with the setup!

## Environment

Let's save ourselves sometimes by configuring the environment. Open the `profile` file with `vim`:

```bash
vim ~/.profile
```

Enter the `INSERTION` vim mode with `i`. Then copy paste (Shift + Insert) the following the configuration:

```bash
# ~/.profile

# https://github.com/huygn/til/issues/26
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2= agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi

unset env

# Open Sublime Text from Git Bash
alias subl="/c/Program\ Files/Sublime\ Text\ 3/subl.exe"

# Python specifics
alias python="winpty python" # https://stackoverflow.com/a/33696825/197944
alias pr="pipenv run"
alias prp="pipenv run winpty python"
alias nosetests="pipenv run winpty nosetests --traverse-namespace"
```

Save and quit with `Esc`, `:wq` and `Enter`. Close and start again Git Bash. It should ask for your SSH key passphrase as it stores it in the SSH agent. This way you won't have to re-type it for every `git` command further on.

## Sublime Text

This text editor comes with great support for Python coding, still experience can be improved with installing the following from Package Control. To install a package, hit `Ctrl` + `Shift` + `P` top open the _command palette_. Then type `install` to select the `Package Control: Install Package` option, type `Enter`. For a few seconds it will load a list of repositories. Then look for the first one in the list. Repeat the process for every item in the list:

- A File Icon (Restart Sublime after installing this one)
- Magic Python
- PowerShell

Then open the preferences (`Preferences > Settings` in the menu). On the right panel, you will find a JSON you can override with the following:

```json
{
  "ensure_newline_at_eof_on_save": true,
  "folder_exclude_patterns": [
    "__pycache__",
    ".git"
  ],
  "highlight_modified_tabs": true,
  "hot_exit": false,
  "ignored_packages": [
    "Python",
    "Vintage"
  ],
  "overlay_scroll_bars": "enabled",
  "remember_open_files": false,
  "rulers": [ 80 ],
  "tab_size": 4,
  "translate_tabs_to_spaces": true,
  "trim_automatic_white_space": true,
  "trim_trailing_white_space_on_save": true,
}
```

You can also go to `View > Hide Minimap`.

Last but not least, a keyboard shortcut is `Ctrl-K`, `Ctrl-B` to open/close the file drawer on the left. Closing it allows you to focus on a single file. To switch files, you don't have to click on the file drawer, you can just type `Ctrl` + `P` and start typing the filename / select it in the list. Very handy to switch files!

## Docker

Time to install **Docker** on your computer ! 🐳 You will need it for day 5.

:point_right: If you were issued a physical Laptop from Le Wagon, it should already be installed: look for the **Docker Desktop** app. **If it is already here, you can skip this part !**

:point_right: We will use the **Community Edition** (which is free and more than enough for our training purpose 👌!)

---

#### ⛔️ **WINDOWS USERS ONLY** - Install Docker on Windows
**Docker Desktop for Windows** is the Community version of Docker for Microsoft Windows.  
You can download Docker Desktop for Windows from Docker Hub.

* Head over to 👉 [this page](https://docs.docker.com/docker-for-windows/install/) and click the "Download from Docker Hub" button
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/download-docker-on-windows.png?raw=true" width="900"></p>
* Follow the installation steps provided by the Docker documentation for your machine

<details><summary markdown='span'><b>⚠️ Details for laptops provided by Le Wagon ⚠️</b></summary>

:point_right: After being redirected, click on <b>"Get Docker Desktop for Windows (stable)"</b>
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/download-docker-on-windows-stable.png?raw=true" width="800"></p>
<br>
:point_right: Once the download is done, double-click the program `Docker Desktop Installer.exe` to run the installer
<br>
:point_right: You will be asked whether you want to <b>"allow this app to make changes to your device"</b>: click <b>"Yes"</b> !
<br>
:point_right_: If prompted, ensure that:
<ul>
  <li>"Enable Hyper-V Windows Features" is <b>enabled</b></li> 
  <li>"Add shortcut to Desktop" is <b>enabled</b></li>
  <li>"Install required Windows components for WSL2" is <b>disabled</b></li>
</ul>
<br>
:point_right: Follow the instructions on the installation wizard to authorize the installer and proceed with the install.
<br>
:point_right: When the installation is successful, click <b>"Close"</b> to complete the installation process.
<br>
:point_right: You might have to restart Windows to complete your installation: if asked, please do so !

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/restart_windows.png?raw=true" width="500"></p>
<br>
⚠️ Do not forget to <b>start</b> Docker Desktop !
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-desktop.png?raw=true" width="400"></p>
<br>
:point_right: When the whale icon in the status bar stays steady, Docker Desktop is up-and-running, and is accessible from any terminal window.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/status-bar.png?raw=true" width="250"></p>
<br>
:point_right: Note that if you do not see the whale, you might have to click on the up-arrow on the taskbar !
<br>
✅ That's it ! You're done !
</details>

<details><summary markdown='span'><b>⚠️ ONLY IF WHALE ICON TURNS RED AFTER INSTALLATIOn. OTHERWISE PLEASE SKIP ⚠️</b> If after 5 minutes, the whale icon is still not steady and turns red, follow these guidelines.</summary>

:point_right: Try to use the Hyper-V backend and not WSL2:
<ul>
<li>In the Docker Desktop app, go to <b>"Settings"</b></li>
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker_desktop_settings.png?raw=true" width="600"></p>
<li>Uncheck the <b>"Use the WSL 2 based engine"</b> option</li>
<li>Click on <b>"Apply & Restart"</b></li>
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/uncheck_wsl.png?raw=true" width="600"></p>
<li>The whale should get steady and white. If not, please ask a TA for help.</li>
</ul>

</details>

<details><summary markdown='span'><b>⚠️ ONLY IF INSTALLATION CRASHES AND YOU ARE ASKED TO "Enable virtualization in the BIOS" ⚠️</b> Please double check with a TA before following these guidelines.</summary>
  
:point_right: This error is a bit tricky to solve, but do not worry, we are here to help ! It means Docker Desktop was not able to use Hyper-V and will have to use WSL 2.
<ul>
<li>You need to activate Virtualization in the BIOS - the easiest way to do it is to watch <a href="https://www.youtube.com/watch?v=MOuTxfzCvMY">this YouTube video</a> and replicate the actions
</li>
<li>Once this is done, you might have to update the WSL 2 Linux Kernel: follow <a href="https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package">these steps</a>
</li>
<li>Relaunch Docker Desktop, and the whale icon should turn white and steady</li>
</ul>

</details>

---

#### ⛔️ **MAC USERS ONLY** - Install Docker on MacOS
**Docker Desktop for Mac** is the Community version of Docker for MacOS. You can download Docker Desktop for Mac from Docker Hub.

* Head over to 👉 [this page](https://docs.docker.com/docker-for-mac/install/) and click the "Download from Docker Hub" button.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/download-docker-on-mac.png?raw=true" width="700"></p>

* Double-click `Docker.dmg` to open the installer, then drag the Docker icon to the Applications folder.

* ⚠️ Do not forget to **start** Docker Desktop !

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-desktop-mac.png?raw=true" width="400"></p>

* When the whale icon in the status bar stays steady, Docker Desktop is up-and-running, and is accessible from any terminal window.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/status-bar-mac.png?raw=true" width="300"></p>

## About Git Bash copy/paste

**Copy from Git Bash:**

Go to your Git Bash terminal and `select text` (`let it highlighted`).
Then, go to your target (another editor, a web browser, etc.) and paste using `CTRL+V` keyboard shortcut.

**Common error:**

Here is the scenario:
I copy some text ex: "git --version") using `CTRL+C` keyboard shortcut (outside of my Git Bash terminal).
I want to paste using `CTRL+V` keyboard shortcut twice (it's a misake, I'm only human).
Then an error message appears : `"bash: $'\302\226': command not found"`
No worries, it's only the keyboard shortcut interpreted as a special char.

**Conlusion: Avoid to use keyboard shortcuts in Git Bash.**

PS: You can use keyboard shortcut (for copy/paste too) if you find how to activate `quick edition` option in yout Git Bash settings. It depends of your Git Bash version. (`Don't waste too much time with it`)
PS2: If you find another solution, please let us know, we'll update this page.

## Exercises

The repository which you just forked contains all the exercises for the week. To work on them, clone them on your laptop. Still in Git Bash, run:

```bash
mkdir -p ~/code/<user.github_nickname> && cd $_
git clone git@github.com:<user.github_nickname>/reboot-python.git
cd reboot-python
git remote add upstream git@github.com:lewagon/reboot-python.git

pwd # This is your exercise repository!
```

This repository has a `Pipfile`. You now can easily install dependencies with the following command:

```bash
pipenv install --dev # to install `packages` **and** `dev-packages`
```

It will create the Virtualenv for this folder, using Python 3.8 as [specified](https://github.com/lewagon/reboot-python/blob/master/Pipfile#L15-L16)

## Getting the green dot

For each challenge, we encourage you to **commit** and **push** your progression. Let's start now with:

```bash
cd 00-Setup
touch READY
git add READY
git commit -m "I am ready"
git push origin master
```

You should get a green dot in the left to track your progression. Cheers!