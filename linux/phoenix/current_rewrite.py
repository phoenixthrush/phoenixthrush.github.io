#!/usr/bin/env python3
import os
import time
import shutil
import random
import argparse
import subprocess
from sys import platform

def phoenixparse():
    parser = argparse.ArgumentParser(usage="phoenixsploit [--sudo --update --remove]")
    parser.add_argument("--sudo", help="uh instantly starting tool with admin rigths!", action="store_true")
    parser.add_argument("--update", help="uh installs or updates phoenixsploit", action="store_true")
    parser.add_argument("--remove", help="uh it uninstalls phoenixsploit", action="store_true")
    parser.add_argument("--ilovecats", help="uh it shows an easter egg which isn´t an easteregg anymore", action="store_true")

    return parser.parse_args()

def first_time():
    os.system("sudo mkdir -p /etc/phoenixthrush")
    os.system("sudo chmod 777 /etc/phoenixthrush")

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def user_exit():
    time.sleep(2)
    clear()
    print("\033[96mThanks for using!")
    print("Have a nice Day!\033[00m \033[31m<3\033[31m")
    print(r"""
               ___
              (___)
       ____
     _\___ \  |\_/|
    \     \ \/ , , \ ___
     \__   \ \ ="= //|||\
      |===  \/____)_)||||
      \______|    | |||||
          _/_|  | | =====
         (_/  \_)_)
      _________________
     (                _)
      (__   '          )
        (___    _____)
            '--'
        """)
    print("\033[00m")
    time.sleep(3)
    exit()

def random_cat():
    cat = random.randint(1, 10)
    if cat == 1:
        asian_cat_1()
        exit()
    elif cat == 2:
        asian_cat_2()
        exit()
    elif cat == 3:
        asian_cat_3()
        exit()
    elif cat == 4:
        asian_cat_4()
        exit()
    elif cat == 5:
        asian_cat_5()
        exit()
    elif cat == 6:
        asian_cat_6()
        exit()
    elif cat == 7:
        asian_cat_7()
        exit()
    elif cat == 8:
        asian_cat_8()
        exit()
    elif cat == 9:
        asian_cat_9()
        exit()
    elif cat == 10:
        asian_cat_10()
        exit()
    else:
        print()
        print("\033[31mError sorry buddy!\033[00m")
    exit()

def asian_cat_1():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
        _..---...,""-._     ,/}/)
     .''        ,      ``..'(/-<
    /   _      {      )         \
   ;   _ `.     `.   <         a(
 ,'   ( \  )      `.  \ __.._ .: y
(  <\_-) )'-.____...\  `._   //-'
 `. `-' /-._)))      `-._)))
   `...'            my asian cat <3
    """)
    print("\033[00m")

def asian_cat_2():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
    """)
    print("\033[00m")

def asian_cat_3():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
     """)
    print("\033[00m")

def asian_cat_4():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |            | /
  )  |  \  `.___________|/
  `--'   `--'
     """)
    print("\033[00m")

def asian_cat_5():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
*bug* .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
     """)
    print("\033[00m")

def asian_cat_6():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
           ___
          (___)
   ____
 _\___ \  |\_/|
\     \ \/ , , \ ___
 \__   \ \ ="= //|||\
  |===  \/____)_)||||
  \______|    | |||||
      _/_|  | | =====
     (_/  \_)_)
  _________________
 (                _)
  (__   '          )
    (___    _____)
        '--'
    """)
    print("\033[00m")

def asian_cat_7():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
        _,'|             _.-''``-...___..--';)
       /_ \'.      __..-' ,      ,--...--'''
      <\    .`--'''       `     /'
       `-';'               ;   ; ;
 __...--''     ___...--_..'  .;.'
(,__....----'''       (,..--''   *asian meow*
    """)
    print("\033[00m")

def asian_cat_8():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
(:`--..___...-''``-._             |`._
  ```--...--.      . `-..__      .`/ _\  
            `\     '       ```--`.    />
            : :   :               `:`-'
             `.:.  `.._--...___     ``--...__      
                ``--..,)       ```----....__,) *bug*
    """)
    print("\033[00m")

def asian_cat_9():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
              __..--''``---....___   _..._    __
    /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
   ///_.-' _..--.'_    \                    `( ) ) // //
   / (_..-' // (< _     ;_..__               ; `' / ///
    / // // //  `-._,_)' // / ``--...____..-' /// / //
        """)
    print("\033[00m")

def asian_cat_10():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
       ,
       \`-._           __
        \\  `-..____,.'  `.
         :`.         /    \`.
         :  )       :      : \
          ;'        '   ;  |  :
          )..      .. .:.`.;  :
         /::...  .:::...   ` ;
         ; _ '    __        /:\
         `:o>   /\o_>      ;:. `.
        `-`.__ ;   __..--- /:.   \
        === \_/   ;=====_.':.     ;
         ,/'`--'...`--....        ;
              ;                    ;
            .'                      ;
          .'                        ;
        .'     ..     ,      .       ;
       :       ::..  /      ;::.     |
      /      `.;::.  |       ;:..    ;
     :         |:.   :       ;:.    ;
     :         ::     ;:..   |.    ;
      :       :;      :::....|     |
      /\     ,/ \      ;:::::;     ;
    .:. \:..|    :     ; '.--|     ;
   ::.  :''  `-.,,;     ;'   ;     ;
.-'. _.'\      / `;      \,__:      \
`---'    `----'   ;      /    \,.,,,/
                   `----`              *meow*
        """)
    print("\033[00m")

def check_sudo(verbose = False, req_perm = False, admin = True):

    if admin is True:
        sudo = os.getuid()
        if sudo == 0:
            if verbose is True:
                print("\033[96mRunning as \033[31mroot\033[96m!\033[00m")
            else:
                return sudo
        else:
            if verbose is True:
                if req_perm is True:
                    print("\033[31mRequesting admin rights!\033[00m")
                    rerun_sudo()
                    exit()
                else:
                    print("\033[31mRunning with \033[96mnormal \033[31muser rights!\033[00m")
            else:
                if req_perm is True:
                    time.sleep(2)
                    rerun_sudo()
                    exit()
                else:
                    return sudo
    else:
        sudo = os.getuid()
        if sudo != 0:
            if verbose is True:
                print("\033[31mRunning with \033[96mnormal \033[31muser rights!\033[00m")
            else:
                return sudo
        else:
            if verbose is True:
                if req_perm is True:
                    print("\033[31mRequesting normal user rights!\033[00m")
                    time.sleep(2)
                    rerun_sudo()
                    exit()
                else:
                    print("\033[31mRunning with \033[96mnormal \033[31muser rights!\033[00m")
            else:
                if req_perm is True:
                    time.sleep(2)
                    rerun_sudo()
                    exit()
                else:
                    return sudo

def check_os_platform(verbose = True):
    system = platform

    if system == "darwin":
        if verbose is True:
            print("\033[31mMacOS detected!\033[00m")
            exit()
        else:
            return system
    elif system == "win32":
        if verbose is True:
            print("\033[31mWindows detected!\033[00m")
            exit()
        else:
            return system
    else:
        os.system("grep -m 1 \"ID=\" /etc/os-release > /etc/phoenixthrush/os.txt")
        with open("/etc/phoenixthrush/os.txt", "r") as f:
            content = f.read()

        if verbose is True:
            if content == "ID=arch\n":
                print("\033[31mArch based Distro detected!\033[00m")
            elif content == "ID=blackarch\n":
                print("\033[31mArch based Distro detected!\033[00m")
            elif content == "ID=debian\n":
                print("\033[31mDebian based Distro detected!\033[00m")
            elif content == "ID=ubuntu\n":
                print("\033[31mDebian based Distro detected!\033[00m")
            elif content == "ID=kali\n":
                print("\033[31mDebian based Distro detected!\033[00m")
            else:
                print("\033[31mCould not detect your distro!\033[00m")
                print("\033[31mExiting!\033[00m")
                user_exit()
        else:
            return content

def check_os_compatibility(verbose = True):
    system = platform

    if system == "darwin":
        if verbose is True:
            print("\033[31mThis Script doesn´t support MacOS yet!\033[00m")
            exit()
        else:
            return system
    elif system == "win32":
        if verbose is True:
            print("\033[31mThis Script doesn´t support Windows yet!\033[00m")
            exit()
        else:
            return system

def rerun_sudo(sudo = True):
    if sudo is True:
        current = (os.path.abspath(__file__))
        current = "sudo " + current
        os.system(current)
        exit()
    else:
        current = (os.path.abspath(__file__))
        os.system(current)
        exit()

def menue():
    clear()
    print("\033[95mWelcome to Phoenixsploit v.4.3\033[00m")
    check_sudo(True)
    print("\033[95m  ___                   ___   ")
    print(" (o o)                 (o o)  ")
    print("(  V  ) \033[96mPhoenixthrush\033[95m (  V  )")
    print("--m-m-------------------m-m--\033[00m")
    print()
    print("\033[31mThis Tool has full support for Debian Based Distros!")
    print("Full Support for Arch and Windows will be coming soon!")
    print("Have Fun <3\033[0;0m")
    print()
    print("\033[92m1 - watch hentai")
    print("2 - destroy ur pc")
    print("3 - real hacking shit")
    print("4 - Install and Update\033[00m \033[31m<3\033[00m")
    print("\033[92m5 - Remove phoenixsploit")
    print("6 - Run as\033[00m \033[31msudo\033[00m")
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
        install_or_update()
        exit()
    elif choice == 5:
        uninstall_phoenixsploit()
        exit()
    elif choice == 6:
        rerun_sudo()
        exit()
    elif choice == 666:
        random_cat()
        exit()
    elif choice == 0:
        user_exit()
        exit()
    else:
        menue()
        exit()

def watch_hentai():
    print("hentai menue")

def destroy_pc():
    print("destroy menue")

def second_menue():
    print("second menue")

def install_or_update():
    print("install or update menue")

def uninstall_phoenixsploit():
    print("uninstall menue")

if __name__ == "__main__":
    phoenixargs = phoenixparse()
    check_os_compatibility()
    first_time()

    if phoenixargs.sudo is True:
        check_sudo(True, True)
    if phoenixargs.update is True:
        exit()
    if phoenixargs.remove is True:
        exit()
    if phoenixargs.ilovecats is True:
        random_cat()
        exit()

    menue()
