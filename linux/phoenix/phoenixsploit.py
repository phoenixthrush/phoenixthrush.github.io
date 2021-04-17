#!/usr/bin/env python3
import os
import time
import shutil
import subprocess

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
        print("\033[31mTrying to request admin rigths!\033[00m")
        time.sleep(3)
        current_file = (os.path.abspath(__file__))
        current_file_new = "sudo " + current_file
        os.system(current_file_new)
        exit()

def check_not_sudo():
    if get_sudo_info() == False:
        print()
        print("\033[31mRunning as standart user!\033[00m")
    else:
        clear()
        print("\033[31mPlease run this script with standart user rigths!\033[00m")
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
        print()
    elif get_os_info() == "Arch":
        print("\033[31mYour System is based on Arch right?\033[00m")
        print()
    else:
        print("\033[31mIdk what your OS is based on!")
        print("I´m sorry but this tool only supports Debian and Arch based distros!\033[00m")
        print()

def get_package_info(package):
    status = subprocess.getstatusoutput("dpkg-query -W -f='${Status}' " + package)
    if not status[0]:
        return True
    else:
        return False

def check_package(package):
    if get_package_info(package) == True:
        print("\033[96m" + package + "\033[00m\033[31m is installed!\033[00m")
        return True
    else:
        print("\033[96m" + package + "\033[00m\033[31m is not installed!\033[00m")
        print("\033[95mTrying to install it!\033[00m")
        print()
        tmp_package = "sudo apt install " + package + " -y"
        if get_os_info() == "Debian":
            os.system(tmp_package)
        elif get_os_info() == "Arch":
            os.system("sudo pacman -Syu firefox --needed --noconfirm")
        else:
            print("\033[31mNot Debian or Arch based!\033[00m")
        return False

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
    print("\033[95mWelcome to Phoenixloit v.3.4")
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
    print("\033[92m5 - Remove phoenixsploit!\033[00m")

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
    elif choice == 5:
        remove_phoenixsploit()
        exit()
    elif choice == 0:
        user_exit()
        exit()
    else:
        menue()
        exit()

def watch_hentai():
    clear()
    check_not_sudo()
    if check_package("firefox") == True:
        print()
        print("\033[32mOkay buddy let me help you!")
        os.system("firefox -new -tab ´https://hentaihaven.xxx´")
    else:
        print()
        print("\033[31mCouldn´t install a programm!\033[00m")

def destroy_pc():
    clear()
    print("Destroyed!")
    print("Just kidding")

def second_menue():
    clear()
    check_sudo()
    check_os()
    hack_menue()
    user_exit()

def install_and_update():
    clear()
    check_sudo()
    print()
    check_package("wget")
    check_package("python3")
    if os.path.exists("/etc/phoenixthrush/update"):
        print()
        print("\033[96mOld files found!\033[00m")
        print("\033[96mDeleting old files\033[00m")
        os.system("sudo rm -rf /etc/phoenixthrush/update")
        os.system("sudo rm -r /etc/phoenixthrush/update")
        os.system("sudo rm /etc/phoenixthrush/phoenixsploit")
        print("\033[96mDeleted old files!\033[00m")
    else:
        install_and_update_2()
        exit()

def install_and_update_2():
    print()
    print("\033[96mCreating new Directory\033[00m")
    os.system("mkdir -p /etc/phoenixthrush")
    os.system("mkdir -p /etc/phoenixthrush/update")
    print("\033[96mDownloading files!\033[00m")
    print()
    os.system("wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/phoenix/install.py")

    current_dir = os.getcwd()
    current_dir += "/install.py"
    original = current_dir
    target = "/etc/phoenixthrush/update"
    shutil.move(original, target)

    if os.path.exists("/bin/phoenixupdate"):
        os.system("sudo rm /bin/phoenixupdate")
    else:
        pass
    
    x = open("/bin/phoenixupdate", "x")
    x.write("clear && sudo bash /etc/phoenixthrush/update/install.py")
    os.system("sudo chmod +x /bin/phoenixupdate")
    os.system("sudo chmod 777 /bin/phoenixupdate")

    os.system("sudo bash /etc/phoenixthrush/update/install.py")
    print()
    print("\033[31mUpdated!\033[00m")
    print("\033[31mYou can also run phoenixupdate to update phoenixsploit!\033[00m")

def remove_phoenixsploit():
    clear()
    check_sudo()
    print("\033[31mTrying to remove phoenixsploit!\033[00m")
    os.system("sudo rm -rf /etc/phoenixthrush")

    if os.path.exists("/bin/phoenixsploit"):
        os.system("sudo rm /bin/phoenixsploit")
    else:
        pass
    
    if os.path.exists("/bin/phoenixphish"):
        os.system("sudo rm /bin/phoenixphish")
    else:
        pass
    
    if os.path.exists("/bin/phoenixupdate"):
        os.system("sudo rm /bin/phoenixupdate")
    else:
        pass
    
    print("\033[31mSuccessfully uninstalled it!\033[00m")
    print()
    print("\033[96mWe had a good time, see ya!\033[31m")
    print("\033[96mAnd have a nice Day!\033[31m \033[31m<3\033[00m")
    print()

def hack_menue():
    print("\033[95mHack Menue\033[00m")
    print()
    print("\033[96m1 - Create a Minecraft-Server")
    print("2 - Create a hidden hotspot")
    print("3 - Website Phishing (blackeye)")
    print("4 - Install common tools")
    print("5 - Update Linux")
    print("6 - Install Arch Linux\033[00m \033[31m<3\033[00m")
    print()
    print("\033[34m0 - Back to menue!\033[00m")
    print()

    try:
        choice = int(input("\033[92mPlease choose a option! \033[00m"))
    except ValueError:
        clear()
        hack_menue()

    if choice == 1:
        minecraft_server()
        exit()
    elif choice == 2:
        hidden_hotspot()
        exit()
    elif choice == 3:
        website_phishing()
        exit()
    elif choice == 4:
        common_tools()
        exit()
    elif choice == 5:
        update_linux()
        exit()
    elif choice == 6:
        arch_install()
        exit()
    elif choice == 0:
        menue()
        exit()
    else:
        menue()
        exit()

def minecraft_server():
    clear()
    print("\033[31mInstalling Minecraft Server!\033[00m")

def hidden_hotspot():
    clear()
    print("\033[31mComing soon!\033[00m")

def website_phishing():
    clear()
    check_sudo()
    print()
    print("\033[31mStarting blackeye!\033[00m")
    print("\033[96mChecking for requests!\033[00m")
    check_package("php")
    print()
    if os.path.exists("/etc/phoenixthrush/repo"):
        print("\033[31mFound existing repo!\033[00m")
        choice = input("\033[96mDo you want to update it? [y|n] \033[00m")
        if choice == "y":
            print()
            os.system("sudo rm -rf /etc/phoenixthrush/repo")
            os.system("sudo rm -r /etc/phoenixthrush/repo")
            current_dir = os.getcwd()
            tmp_dir = current_dir + "repo"
            tmp_sh = "rm -r " + tmp_dir
            os.system(tmp_sh)

            print("\033[96mDownloading files!\033[00m")
            os.system("git clone https://github.com/phoenixthrush/phoenixthrush.github.io repo")
            print()
            print("\033[96mCopying files!\033[00m")

            current_dir = os.getcwd()
            current_dir += "/repo"
            original = current_dir
            target = "/etc/phoenixthrush/repo"
            shutil.move(original, target)

            print("\033[96mInstalling files!\033[00m")
            x = open("/bin/phoenixphish", "x")
            x.write("clear && sudo bash /etc/phoenixthrush/repo/linux/blackeye/blackeye.sh")
            os.system("sudo chmod +x /bin/phoenixphish")
            os.system("sudo chmod 777 /bin/phoenixphish")
            print()
            print("\033[31mYou can start it with phoenixphish\033[00m")
        elif choice == "n":
            clear()
            os.system("sudo bash /etc/phoenixthrush/repo/linux/blackeye/blackeye.sh")
    else:
        print("\033[96mNo old files found!\033[00m")
        print("\033[96mDownloading files!\033[00m")
        print()
        os.system("git clone https://github.com/phoenixthrush/phoenixthrush.github.io repo")
        print()
        print("\033[96mCopying files!\033[00m")

        current_dir = os.getcwd()
        current_dir += "/repo"
        original = current_dir
        target = "/etc/phoenixthrush/repo"
        shutil.move(original, target)

        print("\033[96mInstalling files!\033[00m")
        x = open("/bin/phoenixphish", "x")
        x.write("clear && sudo bash /etc/phoenixthrush/repo/linux/blackeye/blackeye.sh")
        os.system("sudo chmod +x /bin/phoenixphish")
        os.system("sudo chmod 777 /bin/phoenixphish")
        print()
        print("\033[31mYou can start it with phoenixphish\033[00m")

def common_tools():
    clear()
    print("\033[31mInstalling common tools!\033[00m")
    print()

def update_linux():
    clear()
    check_sudo()
    if get_os_info() == "Debian":
        os.system("apt update -y")
        os.system("sudo apt full - upgrade -y")
        os.system("sudo apt autoremove -y")

    print()
    print("\033[31mUpdating Linux!\033[00m")
    print()

def arch_install():
    clear()
    print("\033[31mStarting Arch installation!\033[00m")
    print()
    if os.path.exists("/etc/phoenixthrush/arch"):
        print("\033[31mOld files for Arch installation detected!\033[00m")
        choice = input("\033[96mDo you want to remove the old files? [y|n] \033[00m")
        if choice == "y":
            print()
            os.system("rm -rf /etc/phoenixthrush/arch")
            print("\033[31mOld files removed!\033[00m")
            arch_install_step_2()
            exit()

        elif choice == "n":
            print()
            print("\033[31mexiting!\033[00m")
            time.sleep(3)
            user_exit()
            exit()
    else:
        arch_install_step_2()
        exit()

def arch_install_step_2():
    print()
    print("Credits picodotdev")
    print("https://github.com/picodotdev")
    print()
    print("WARNING! All data will be erased!")
    print("Unplug all Drives that are not needed!")
    print()
    print("Please burn the official Arch Live ISO to the USB!")
    print("Boot into it and type: loadkeys [ur keymap like de-latin1 for germany]")
    print()
    print("Edit the alis.conf and alis-packages.conf")
    print("Default password is phoenixthrush")
    print()
    input(("\033[95mPress Enter to continue! \033[00m"))
    arch_install_step_3()
    exit()

def arch_install_step_3():
    print()
    print("\033[96mCreating new Directory at /etc/phoenixthrush/arch\033[00m")
    os.system("mkdir -p /etc/phoenixthrush")
    os.system("mkdir /etc/phoenixthrush/arch")
    print("\033[96mDownloading files that are needed to /etc/phoenixthrush/arch\033[00m")
    print()
    os.system("curl https://raw.githubusercontent.com/picodotdev/alis/master/download.sh | bash")
    os.system("rm alis.conf")
    os.system("rm alis-packages.conf")
    os.system("wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/alis.conf")
    os.system("wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/alis-packages.conf")

    current_dir = os.getcwd()
    current_dir += "/alis-asciinema.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-asciinema.sh"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis.conf"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis.conf"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-packages-asciinema.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-packages-asciinema.sh"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-packages.conf"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-packages.conf"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-packages.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-packages.sh"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-reboot.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-reboot.sh"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-recovery-asciinema.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-recovery-asciinema.sh"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-recovery.conf"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-recovery.conf"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-recovery-reboot.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-recovery-reboot.sh"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis-recovery.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis-recovery.sh"

    shutil.move(original, target)

    current_dir = os.getcwd()
    current_dir += "/alis.sh"

    original = current_dir
    target = "/etc/phoenixthrush/arch/alis.sh"

    shutil.move(original, target)

    print()
    print("\033[96mEditing config files for you!\033[00m")
    choice = input("\033[96mDo you want to manually edit them? [y|n] \033[00m")
    if choice == "y":
        print("\033[96mEditing Files!\033[00m")
        os.system("nano /etc/phoenixthrush/arch/alis.conf")
        os.system("nano /etc/phoenixthrush/arch/alis-packages.conf")
        print("\033[96mManually edited files!\033[00m")
        print()
        tmp = input("\033[95mPress Enter to start installation! \033[00m")
        arch_install_step_4()
        exit()

    elif choice == "n":
        print("\033[96mUsing default configs!\033[00m")
        arch_install_step_4()
        exit()
    else:
        arch_install_step_3()
        exit()

def arch_install_step_4():
    print()
    os.system("cd /etc/phoenixthrush/arch && sudo ./alis.sh")
    print()
    print("\033[96mCleaning up files!\033[00m")
    os.system("rm -rf /etc/phoenixthrush/arch")
    print("\033[96mCleaned files!\033[00m")

menue()
