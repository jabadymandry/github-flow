# Setup

## Physical Laptop

If you were issued a physical Laptop from Le Wagon, here is what should already be there:

- Google Chrome
- [**Sublime Text 3**](https://www.sublimetext.com/) (Unlicensed but unlimited usage) with [Package Control](https://packagecontrol.io/) installed.
- [Python 3.8](https://www.python.org/downloads/) & [`pip install pipenv`](https://pipenv.pypa.io/en/latest/)
- `git` with [**Git Bash**](https://git-scm.com/downloads) which will be your main command line tool this week.

## Upgrade package managers (pip, pipenv)

Open the Windows Command Prompt **as Administrator** (in your search menu, you will see 2 command prompt: the default one, and the Administrator one. Pick the latter !)

Run the following commands:

```bash
pip install --upgrade pip
pip install --upgrade pipenv
```

## Checking your path

Your `$PATH` should be all set to work with the required binaries.

Open Git Bash and check some versions:

```bash
git --version
python --version
pipenv --version
```

## Your turn!

There still some configuration left for **you** to do.

### GitHub

We will use your personal public `github.com` account. If you are reading this, it means that you have one and are logged in with it!

First, ensure to have this repository forked to your own personal github account

We need to create a SSH key on your computer and link it to your GitHub account. At the end of the week, don't forget to remove this key from your GitHub account as this is not your computer. Protecting your key with a strong **passphrase** will guarantee security during the week.

GitHub has handy tutorials. Follow them:

1. [Generate a new SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows)
1. [Add this key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-windows)

To check if this step is done, run:

```bash
ssh -T git@github.com
```

If it says "Permission denied", call a teacher to help you. If it says "Hi <github_nickname>", all good!

At last, we need to configure the local `git` command to tell it who you are when you make a commit:

```bash
git config --global user.email "your_github_email@domain.com"
git config --global user.name "Your Full Name"
```

It's important to use the same email as the one you use on [GitHub](https://github.com/settings/emails) so that [commits are linked to your profile](https://help.github.com/articles/why-are-my-commits-linked-to-the-wrong-user/#commits-are-not-linked-to-any-user).

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
alias prp="pipenv run python"
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
