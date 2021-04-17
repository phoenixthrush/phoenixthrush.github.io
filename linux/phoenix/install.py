#!/usr/bin/python

import subprocess
import shutil
import os

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

clear()
print("\033[31m[*]\033[00m \033[96mStarting installation of phoenixsploit...\033[00m")
print()
print("\033[31m[*]\033[00m \033[96mChecking if old files are installed...\033[00m")

if os.path.exists("/etc/phoenixthrush/phoenixsploit"):
    print("\033[31m[*]\033[00m \033[96mOld files detected...\033[00m")
    os.system("sudo rm /etc/phoenixthrush/phoenixsploit")
    print("\033[31m[*]\033[00m \033[96mOld files removed...\033[00m")
else:
    print("\033[31m[*]\033[00m \033[96mNo old files were found...\033[00m")
    pass

if os.path.exists("/etc/phoenixthrush/phoenixsploit"):
    print("\033[96mFound phoenixsploit in /etc/phoenixthrush\033[00m")
    print("\033[96mRemoving phoenixsploit in /etc/phoenixthrush\033[00m")
    os.system("sudo rm /etc/phoenixthrush/phoenixsploit")
    if os.path.exists("/etc/phoenixthrush/update"):
        print("\033[96mFound dir in /etc/phoenixthrush/update\033[00m")
        print("\033[96mRemoving dir in /etc/phoenixthrush/update\033[00m")
        os.system("sudo rm -rf /etc/phoenixthrush/update")
    else:
        pass
else:
    pass

os.system("mkdir -p /etc/phoenixthrush")
os.system("sudo chmod 777 /etc/phoenixthrush")
print("\033[31m[*]\033[00m \033[96mDownloading package from github...\033[00m")
print()
os.system("wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/phoenix/phoenixsploit.py")
print("\033[31m[*]\033[00m \033[96mMoving files to install dir...\033[00m")
current_dir = os.getcwd()
current_dir += "/phoenixsploit.py"
original = current_dir
target = "/etc/phoenixthrush/phoenixsploit"
shutil.move(original, target)

print("\033[31m[*]\033[00m \033[96mCreating launcher for phoenixsploit...\033[00m")
filewrite = open("/bin/phoenixsploit", "w")
filewrite.write("clear && python3 /etc/phoenixthrush/phoenixsploit")
filewrite.close()
print("\033[31m[*]\033[00m \033[96mDone. Chmoding +x...\033[00m")
os.system("sudo chmod +x /etc/phoenixthrush/phoenixsploit")
os.system("sudo chmod 777 /etc/phoenixthrush/phoenixsploit")
os.system("sudo chmod +x /bin/phoenixsploit")
os.system("sudo chmod 777 /bin/phoenixsploit")
print()
print("\033[31m[*]\033[00m \033[31mFinished. Run 'phoenixsploit' to start it!\033[00m")
print()
