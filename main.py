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
    ans = input("What would you like to do? 1.Install Common Apps Automaticly 2. Install Only Some Common Applications 3. Do Nothing and Exit? ")

if ans == 1:
    print("1. Selected. Installing all common apps with log.")
    