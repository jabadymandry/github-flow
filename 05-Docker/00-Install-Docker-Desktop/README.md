# Install Docker Desktop

Time to install **Docker** on your computer ! 🐳  
We will use the **Community Edition** (which is free and more than enough for our training purpose 👌!)

Do not forget to validate your installation.

---

### ⚠️ **WINDOWS USERS ONLY** ⚠️ Install Docker on Windows
**Docker Desktop for Windows** is the Community version of Docker for Microsoft Windows.  
You can download Docker Desktop for Windows from Docker Hub.

* Head over to 👉 [this page](https://docs.docker.com/docker-for-windows/install/) and click the "Download from Docker Hub" button.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/download-docker-on-windows.png?raw=true" width="800"></p>

* Then, after being redirected, click on **"Get Docker Desktop for Windows (stable)"**

* Once the download is done, double-click the program `Docker Desktop Installer.exe` to run the installer

* You will be asked whether you want to **"allow this app to make changes to your device"**: click **"Yes"** !

* If prompted, ensure that the **"Enable Hyper-V Windows Features"** and **"Add shortcut to Desktop"** options are selected on the configuration page

* Follow the instructions on the installation wizard to authorize the installer and proceed with the install.

* When the installation is successful, click **"Close"** to complete the installation process.

* You might have to restart Windows to complete your installation: if asked, please do so !

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/restart_windows.png?raw=true" width="400"></p>

* ⚠️ Do not forget to **start** Docker Desktop !

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-desktop.png?raw=true" width="300"></p>

* When the whale icon in the status bar stays steady, Docker Desktop is up-and-running, and is accessible from any terminal window.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/status-bar.png?raw=true" width="250"></p>
Note that if you do not see the whale, you might have to click on the up-arrow on the taskbar !
<br><br>
✅ That's it ! You're done !
<br><br>
<details><summary markdown='span'><b>⚠️ ONLY IF WHALE ICON TURNS RED. OTHERWISE PLEASE SKIP ⚠️</b> If after 5 minutes, the whale icon is still not steady and turns red, follow these guidelines.</summary>
<ul>
	<li>In the Docker Desktop app, go to <b>"Settings"</b></li>
	<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker_desktop_settings.png?raw=true" width="500"></p>
	<li>Uncheck the <b>"Use the WSL 2 based engine"</b> option</li>
	<li>Click on <b>"Apply & Restart"</b></li>
	<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/uncheck_wsl.png?raw=true" width="500"></p>
	<li>The whale should get steady and white. If not, please ask a TA for help.</li>
</ul>

</details>

---

### ⚠️ **MAC USERS ONLY** ⚠️ Install Docker on MacOS
**Docker Desktop for Mac** is the Community version of Docker for Microsoft Windows. You can download Docker Desktop for Mac from Docker Hub.

* Head over to 👉 [this page](https://docs.docker.com/docker-for-mac/install/) and click the "Download from Docker Hub" button.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/download-docker-on-mac.png?raw=true" width="700"></p>

* Double-click Docker.dmg to open the installer, then drag the Docker icon to the Applications folder.

* ⚠️ Do not forget to **start** Docker Desktop !

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-desktop-mac.png?raw=true" width="400"></p>

* When the whale icon in the status bar stays steady, Docker Desktop is up-and-running, and is accessible from any terminal window.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/status-bar-mac.png?raw=true" width="300"></p>
<br>
✅ That's it ! You're done !

---

### Installation validation ✅ 

You can now close the Docker Desktop window, as it is now running in the background.

#### Signup on Docker Hub 💻
Docker Hub is a hosted repository service provided by Docker for finding and sharing container images with your team. Once you create a Docker ID (a user), you will be able to pull and push images to the Hub.

Create a personal account 👉  [here](https://hub.docker.com/signup).

#### Login

Open a terminal and type:
```bash
docker login
```

You will be prompted for your username and password:
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-login.png?raw=true" width="700"></p>

When successful, your terminal should tell you "Login Succeeded" 🙌! 

#### Hello-World !

Let's validate our Docker installation by running our first container: `hello-world`. To do so, run the following in your terminal:

```bash
docker run hello-world
```

Since you do not have any docker images on your host (as you just installed docker), 

* it will first pull the `hello-world` image from the Hub
* then run a container from this image (this one _only_ prints a message)

You should end up with something like this:
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/hello-world.png?raw=true" width="700"></p>


##### To see the containers you have running on your hosts 👀:

```
docker ps
```

You don't see any 🤔 ? That's normal !   
Your `hello-world` container is not running anymore: it exited as soon as it was done. Its job was simply to print a message.

##### To view all containers (even non-running ones), run:
```
docker ps -a
```

You should see a container here. What is its name ? Which image was used to run it ? What is its state ?

##### To view images on your host:
```
docker images
```

You should see your `hello-world` image, freshly pulled. You also have access to other details such as 

* the image ID, 
* the image tag (used to convey important information about the image. By default, the tag is "latest". You can have a look at [this list of tags](https://hub.docker.com/_/python): do you understand what they are here for ?),
* the image size

---

## I'm done! 🎉

That's it for this installer, you are good to go to the next challenge where we will deep dive into Docker commands !

But before you jump to it, let's mark your progress with the following:

```bash
cd ~/code/<user.github_nickname>/reboot-python
cd 05-Docker/00-Install-Docker-Desktop
touch DONE.md
git add DONE.md && git commit -m "05-Docker/00-Install-Docker-Desktop done"
git push origin master
```
