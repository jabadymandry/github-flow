# Install Docker Desktop

Time to install **Docker** on your computer ! 🐳    
You will need it for day 5 !

:point_right: We will use the **Community Edition** (which is free and more than enough for our training purpose 👌!)

---

### ⚠️ **WINDOWS USERS ONLY** ⚠️ Install Docker on Windows
**Docker Desktop for Windows** is the Community version of Docker for Microsoft Windows.  
You can download Docker Desktop for Windows from Docker Hub.

* Head over to 👉 [this page](https://docs.docker.com/docker-for-windows/install/) and click the "Download from Docker Hub" button.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/download-docker-on-windows.png?raw=true" width="900"></p>

* Then, after being redirected, click on **"Get Docker Desktop for Windows (stable)"**
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/download-docker-on-windows-stable.png?raw=true" width="800"></p>

* Once the download is done, double-click the program `Docker Desktop Installer.exe` to run the installer

* You will be asked whether you want to **"allow this app to make changes to your device"**: click **"Yes"** !

* If prompted, ensure that:
	* **"Enable Hyper-V Windows Features"** and
	* **"Add shortcut to Desktop"** options are selected on the configuration page

* Follow the instructions on the installation wizard to authorize the installer and proceed with the install.

* When the installation is successful, click **"Close"** to complete the installation process.

* You might have to restart Windows to complete your installation: if asked, please do so !

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/restart_windows.png?raw=true" width="500"></p>

* ⚠️ Do not forget to **start** Docker Desktop !

<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/docker-desktop.png?raw=true" width="400"></p>

* When the whale icon in the status bar stays steady, Docker Desktop is up-and-running, and is accessible from any terminal window.
<p><img src="https://github.com/lewagon/fullstack-images/blob/master/reboot-python/status-bar.png?raw=true" width="250"></p>
Note that if you do not see the whale, you might have to click on the up-arrow on the taskbar !
<br><br>
✅ That's it ! You're done !
<br><br>
<details><summary markdown='span'><b>⚠️ ONLY IF WHALE ICON TURNS RED. OTHERWISE PLEASE SKIP ⚠️</b> If after 5 minutes, the whale icon is still not steady and turns red, follow these guidelines.</summary>

:point_right: You need to make sure you are using the Hyper-V backend and not WSL2:
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