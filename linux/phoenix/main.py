#!/usr/bin/env python3
import os

def get_sudo_info():
    if os.geteuid() == 0:
        admin_check = True
        return admin_check
    else:
        admin_check = False
        return admin_check

def check_sudo():
    if get_sudo_info() == True:
        print("\033[31mRunning as root!\033[00m")
    else:
        print("\033[31mPlease run this tool with admin rights!\033[00m")
        print()
        exit()

def get_os_info():
    if os.name == "posix":
        system = "Debian"
        return system
    elif os.name == "arch":
        system = "Arch"
        return system
    else:
        system = "unknown OS"
        return system

def check_os():
    if get_os_info() == "Debian":
        print("\033[31mYou´re System is based on Debian right?\033[00m")
    elif get_os_info() == "Arch":
        print("\033[31mYou´re System is based on Arch right?\033[00m")
        print()
    else:
        print("\033[31mIdk what your OS is based on!")
        print("I´m sorry but this tool only supports Debian and Arch based distros!\033[00m")
        print()

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def user_exit():
    clear()
    print("\033[96mThanks for using!")
    print("Have a nice Day!\033[00m \033[31m<3\033[00m")
    print()

def menue():
    clear()
    print("\033[95mWelcome v.3.1")
    print("  ___                   ___   ")
    print(" (o o)                 (o o)  ")
    print("(  V  ) \033[96mPhoenixthrush\033[95m (  V  )")
    print("--m-m-------------------m-m--\033[00m")
    print()
    print("\033[31mThis Tool has full support for Arch Linux!")
    print("Full Support for Debian will be coming soon!")
    print("Have Fun <3\033[0;0m")
    print()
    print("\033[92m1 - watch hentai")
    print("2 - destroy ur pc")
    print("3 - real hacking shit")
    print("4 - Install and Update!\033[00m \033[31m<3\033[00m")
    print()
    print("\033[96m0 - exit\033[00m")

    try:
        choice = int(input("\033[34mPlease choose a option! \033[00m"))
    except ValueError:
        clear()
        menue()

    if choice == 1:
        watch_hentai()
        exit()
    elif choice == 2:
        destroy_pc()
        exit()
    elif choice == 3:
        second_menue()
        exit()
    elif choice == 4:
        install_and_update()
        exit()
    elif choice == 0:
        user_exit()
        exit()
    else:
        menue()
        exit()

def watch_hentai():
    clear()
    print("You watched it!")

def destroy_pc():
    clear()
    print("Destroyed!")

def second_menue():
    clear()
    check_sudo()
    check_os()
    print("Hacking Hub")

def install_and_update():
    clear()
    print("Updated!")

menue()
