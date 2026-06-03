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
else:
    rw = False
    lnx = False
    print("Sorry, this program only runs on Windows and Linux.")

if lnx == True:
    os.system("clear")
    print(ascii)
    print("Welcome to ACAOI (Automated Common Apps OS Installer)")
    print("")
    pkg = input("What would you like to do? 1. Install your own package (Using your Distro's package manager) 2. Quit")
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
            os.system(f"winget import host.txt --accept-source-agreements --accept-package-agreements")
        else:
            print("Something other than yes was entered, exiting...")

    
    if "2" in ans:
        print("2. Selected. Installing Set of only some common apps")
        os.system("winget import simple.txt")
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




