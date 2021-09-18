#!/usr/bin/env python3
import os
import argparse

def phoenixparse():
    parser = argparse.ArgumentParser(usage="phoenixsploit [--sudo --update --remove]")
    parser.add_argument("--sudo", help="uh instantly starting tool with admin rigths!", action="store_true")
    parser.add_argument("--update", help="uh installs or updates phoenixsploit", action="store_true")
    parser.add_argument("--remove", help="uh it uninstalls phoenixsploit", action="store_true")
    parser.add_argument("--ilovecats", help="uh it shows an easter egg which isn´t an easteregg anymore", action="store_true")

    return parser.parse_args()

if __name__ == "__main__":
    phoenixargs = phoenixparse()

    if phoenixargs.sudo is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --sudo")
        exit()
    if phoenixargs.update is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --update")
        exit()
    if phoenixargs.remove is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --remove")
        exit()
    if phoenixargs.ilovecats is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --ilovecats")
        exit()

    os.system("python3 /etc/phoenixthrush/phoenixsploit")
