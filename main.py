import os
import time
import sys
import platform


ascii = r"""
    _   ___   _   ___ ___ 
   /_\ / __| /_\ / _ \_ _|
  / _ \ (__ / _ \ (_) | | 
 /_/ \_\___/_/ \_\___/___|
                          
"""
lnx = False
if platform.system() == "Windows":
    rw = True
    os.system("cls")
    print("Running on Windows.")
    time.sleep(0.7)
elif platform.system() == "Linux":
    lnx = True
    print("Running on Linux")
elif platform.system() == "Darwin":
    print("Running on Darwin/macOS.")
    time.sleep(0.7)
    os.system("clear")
    print(ascii)
    print("Welcome to ACAOI (Automated Common Apps OS Installer)")
    print("")
    print("Please note all tasks are done through Homebrew.")
    ans = input("What would you like to do? 1. Install your own package")
    if "1" in ans:
        print("Install own package selected")
        if os.path.exists("/opt/homebrew"):
            print("Homebrew already installed, continuing")
            hbwi = True
        else: 
            hbwi = False
        if hbwi:
            pkgname = input("What package do you want to install?: ")
            time.sleep(0.7)
            os.system(f"brew install --cask {pkgname}")
        else:
            confirm = input("Homebrew needs to be installed, continue?")
            if "yes" in confirm:
                print("Confirmed.")
                time.sleep(0.7)
                os.system("NONINTERACTIVE=1 /bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")
                if os.path.exists("/opt/homebrew"):
                    print("Homebrew installed.")
                    hbwi = True
                if hbwi:
                    print("Please note packages are being installed through Homebrew")
                    print("")
                    time.sleep(0.7)
                    pkgname = input("What package do you want to install?: ")
                    time.sleep(0.7)
                    os.system(f"brew install --cask {pkgname}")

            
else:
    rw = False
    lnx = False
    print("Sorry, this program only runs on Windows, macOS/Darwin and Linux.")

if lnx == True:
    rw = False
    os.system("clear")
    print(ascii)
    print("Welcome to ACAOI (Automated Common Apps OS Installer)")
    print("")
    pkg = input("What would you like to do? 1. Install your own package (Using your Distro's package manager) 2. Install a list of common apps (VS Code, Spotify, Firefox, LibreOffice, Steam etc) 3. Install a browser 4. Quit? :")
    if "1" in pkg:
        print("Installing custom package selected.")
        if os.path.exists("/etc/apt/apt.conf.d"):
            print("Apt detected, using that. ")
            time.sleep(0.7)
            pkg = input("What package do you want to install? (Requires Sudo): ")
            os.system(f"sudo apt install {pkg} -y")
        if os.path.exists("/etc/pacman.conf"):
            print("Pacman detected. Using that")
            time.sleep(0.7)
            pkg = input("What package would you like to install (Requires Sudo): ")
            os.system(f"sudo pacman -Sy {pkg} --noconfirm")
        if os.path.exists("/etc/dnf/dnf.conf"):
            print("DNF detected.")
            time.sleep(0.7)
            pkg = input("What package do you want to install? (Requires Sudo): ")
            os.system(f"sudo dnf install {pkg} -y")
        if os.path.exists("/data/data/com.termux/files/usr"):
            print("Termux detected, using pkg.")
            time.sleep(0.7)
            pkg = input("What package do you want to install?: ")
            os.system(f"pkg install {pkg} -y")
        if os.path.exists("/etc/pkg"):
            print("Pkg detected.")
            time.sleep(0.7)
            pkg = input("What package do you want to install? (Requires Sudo): ")
            os.system(f"sudo pkg install {pkg} -y")
        if os.path.exists("/etc/zypp/zypper.conf"):
            print("Zypper detected.")
            time.sleep(0.7)
            pkg = input("What package do you want to install? (Requires Sudo): ")
            os.system(f"sudo zypper -n install -l {pkg}")
    if "2" in pkg:
        if os.path.exists("/etc/apt/apt.conf.d"):
            print("Apt detected, using that. ") 
            time.sleep(1)
            os.system("sudo apt install steam-installer lutris firefox-esr vlc libreoffice vim nano")
            print("Installing Visual Studio Code...")
            time.sleep(1)
            os.system(f"wget 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64' -O /tmp/code.deb")
            os.system(f"sudo dpkg -i /tmp/code.deb")
            print("Installing Spotify...")
            os.system("curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg")
            os.sysetm(f'echo "deb https://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list"')
            os.system("sudo apt update && sudo apt install spotify-client -y")
            print("Done!")
        if os.path.exists("/etc/pacman.conf"):
            print("Pacman detected. Installing with that")
            yes = input("We need to install paru first. Ok? : ")
            if "yes" in yes:
                print("Allowed.")
                os.system("sudo pacman -Sy git fakeroot gcc debugedit make --noconfirm")
                os.system("git clone https://aur.archlinux.org/yay.git")
                os.system("sudo pacman -S --needed git base-devel")
                os.chdir(f"{os.getcwd()}/yay")
                os.system("makepkg -si --noconfirm")
                if os.path.exists("/usr/bin/yay"):
                    print("Yay installed.")
                    print("Installing most common apps...")
                    os.system("paru -Sy firefox spotify visual-studio-code-bin vlc libreoffice vim nano --noconfirm")
                else: 
                    print("Yay not installed.")
        if os.path.exists("/etc/dnf/dnf.conf"):
            print("Using DNF.")
            time.sleep(0.7)
            print("Instaling common apps...")
            os.system("sudo dnf install firefox lutris vlc steam libreoffice vim nano -y")
            time.sleep(0.7)
            print("Installing Visual Studio Code and Spotify")
            os.system("flatpak install flathub com.visualstudio.code com.spotify.Client -y")
            time.sleep(0.7)
            print("Done!")
        if os.path.exists("/etc/pkg"):
            print("Using PKG.")
            time.sleep(0.7)
            print("Installing common apps...")
            os.system("pkg install firefox vscode libreoffice vim nano -y")
            time.sleep(0.7)
            print("Done!")
    if "3" in pkg:
        print("Browsers selected.")
        time.sleep(0.7)
        if os.path.exists("/etc/apt/apt.conf.d"):
            print("Using APT.")
            browser = input("What browser do you want to install? 1. Firefox ESR 2. Chromium 3. Brave 4. Google Chrome 5. All? :")
            if "1" in browser:
                print("Firefox ESR selected.")
                time.sleep(0.7)
                if os.path.exists("/etc/apt/apt.conf.d"):
                    print("Using apt")
                    os.system("sudo apt install firefox-esr -y")
                if os.path.exists("/usr/bin/firefox-esr") or os.path.exists("/usr/bin/firefox"):
                    print("Done!")
                else:
                    print("Firefox ESR not installed.")
            if "2" in browser:
                print("Chromium selected.")
                time.sleep(0.7)
                if os.path.exists("/etc/apt/apt.conf.d"):
                    print("Using apt.")
                    os.system(f"sudo apt install chromium -y")
                if os.path.exists("/usr/bin/chromium"):
                    print("Chromium installed.")
                else: 
                    print("Chromium not installed.")
            if "3" in browser:
                print("Brave selected.")
                time.sleep(0.7)
                os.system("curl -fsS https://dl.brave.com/install.sh | sh")
                os.system("clear")
                if os.path.exists("/usr/bin/brave-browser"):   
                    print("Brave installed")
                else: 
                    print("Brave not installed.")
                
            if "4" in browser:
                print("Google Chrome selected.")
                time.sleep(0.7)
                os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
                os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
                time.sleep(0.7)
                if os.path.exists("/usr/bin/google-chrome-stable"):
                    print("Chrome installed.")
                else:
                    print("Chrome not installed.")

    

                
            
               
                


            



if rw == True:
    os.system("cls")
    print(ascii)
    print("Welcome to ACAOI (Automated Common Apps OS Installer)")
    print("")
    ans = input("What would you like to do? 1.Install ALL Common Apps Automaticaly 2. Install Only Some Common Applications 3. Install a Web Browser 4. Install your own app 5. Do Nothing and Exit? ")
    if "1" in ans:
        print("1. Selected. Installing all common apps with log.")
        confirm = input("Are you sure you want to do this? This will install 40+ apps on your Computer eg: Firefox, Chrome, Brave, WireShark, Spotify etc: ")
        if "yes" in confirm:
            os.system(f"winget import wa.txt -h --accept-source-agreements --accept-package-agreements")
        else:
            print("Something other than yes was entered, exiting...")

    
    if "2" in ans:
        print("2. Selected. Installing Set of only some common apps")
        os.system("winget import sw.txt -h --accept-source-agreements --accept-package-agreements")
        browser = input('Which browser do you want to install? 1. Firefox 2. Brave 3. Google Chrome 4. Chromium 5. DeGoogled Chromium 6. All: 7: None:  ')
        if "1" in browser:
            print("Firefox selected")
            os.system("winget install Mozilla.Firefox -h --accept-source-agreements --accept-package-agreeements")
        if "2" in browser:
            print("Brave selected.")
            os.system("winget install Brave.Brave -h --accept-source-agreements --accept-package-agreements")
        if "3" in browser:
            print("Google Chrome selected.")
            os.system("winget install Google.Chrome -h --accept-source-agreements --accept-package-agreements")
        if "4" in browser:
            os.system("winget install Hibbiki.Chromium -h --accept-package-agreements --accept-source-agreements")
        if "5" in browser:
            print("DeGoogled Chromium selected.")
            os.system("winget install --id eloston.ungoogled-chromium -h --accept-package-agreements --accept-source-agreements")
        if "6" in browser:
            print("All selected.")
            os.system("winget install Mozilla.Firefox Brave.Brave Google.Chrome Hibbiki.Chromium eleston.ungoogled-chromium --slient --accept-package-agreements --accept-source-agreements")
        else:
            print("None was selected, exiting...")
    if "3" in ans:
        browser = input('Which browser do you want to install? 1. Firefox 2. Brave 3. Google Chrome 4. Chromium 5. DeGoogled Chromium 6. All: ')
        if "1" in browser:
            print("Firefox selected")
            os.system("winget install Mozilla.Firefox -h --accept-source-agreements --accept-package-agreeements")
        if "2" in browser:
            print("Brave selected.")
            os.system("winget install Brave.Brave -h --accept-source-agreements --accept-package-agreements")
        if "3" in browser:
            print("Google Chrome selected.")
            os.system("winget install Google.Chrome -h --accept-source-agreements --accept-package-agreements")
        if "4" in browser:
            print("Chromium selected.")
            os.system("winget install Hibbiki.Chromium -h --accept-package-agreements --accept-source-agreements")
        if "5" in browser:
            print("DeGoogled Chromium selected.")
            os.system("winget install --id eloston.ungoogled-chromium -h --accept-package-agreements --accept-source-agreements")
        if "6" in browser:
            print("All selected.")
            os.system("winget install Mozilla.Firefox Brave.Brave Google.Chrome Hibbiki.Chromium eleston.ungoogled-chromium --slient --accept-package-agreements --accept-source-agreements")
        else: 
            print("None was selected, exiting")

    if "4" in ans:
        app = input("What app do you want to install? (Using WinGet and ID (eg: Valve.Steam) ): ")
        time.sleep(0.3)
        os.system(f"winget install {app}")




