#!/usr/bin/python

from __future__ import print_function
import subprocess
import os
print("[*] Installing phoenixsploit to /etc/phoenixthrush/update...")
os.system("rm /etc/phoenixthrush/phoenixsploit")
os.system("wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/phoenix/phoenixsploit.py")
current_dir = os.getcwd()
current_dir += "/phoenixsploit.py"
original = current_dir
target = "/etc/phoenixthrush/phoenixsploit"
shutil.move(original, target)
print("[*] Creating launcher for phoenixsploit...")
filewrite = open("/bin/phoenixsploit", "w")
filewrite.write("#!/bin/sh\ncd /etc/phoenixthrush/phoenixsploit")
filewrite.close()
print("[*] Done. Chmoding +x.... ")
subprocess.Popen("chmod +x /bin/phoenixsploit", shell=True).wait()
print("[*] Finished. Run 'phoenixsploit' to start it!")
