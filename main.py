import os
import time
import sys
import platform


ascii = r"""
    _   ___   ___      _____ 
   /_\ / __| /_\ \    / /_ _|
  / _ \ (__ / _ \ \/\/ / | | 
 /_/ \_\___/_/ \_\_/\_/ |___|
                             
"""

if platform.system() == "Windows":
    rw = True
    os.system("cls")
    print("Running on Windows.")
    time.sleep(0.7)
else:
    rw = False
    print("Sorry, this program only runs on Windows.")

if rw == True:
    os.system("cls")
    print(ascii)
    print("Welcome to ACAWI (Automated Common Apps Windows Installer)")
    ans = input("What would you like to do? 1.Install ALL Common Apps Automaticaly 2. Install Only Some Common Applications 3. Do Nothing and Exit? ")

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
        os.system("winget install Hibbiki.Chromium -h --accept-package-agreements --accept-source-agreements")
    if "5" in browser:
        print("DeGoogled Chromium selected.")
        os.system("winget install --id eloston.ungoogled-chromium -h --accept-package-agreements --accept-source-agreements")
    if "6" in browser:
        print("All selected.")
        os.system("winget install Mozilla.Firefox Brave.Brave Google.Chrome Hibbiki.Chromium eleston.ungoogled-chromium --slient --accept-package-agreements --accept-source-agreements")

