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
    parser.add_argument("--666", action="store_true")

    return parser.parse_args()

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def user_exit():
    time.sleep(3)
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
    cat = random.randint(1,10)
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

    if admin == True:
        sudo = os.getuid()
        if sudo == 0:
            if verbose == True:
                print("\033[31mRunning as root!\033[00m")
            else:
                return sudo
        else:
            if verbose == True:
                if req_perm == True:
                    print("\033[31mRequesting admin rights!\033[00m")
                    time.sleep(3)
                    run_sudo = (os.path.abspath(__file__))
                    run_sudo = "sudo " + run_sudo
                    os.system(run_sudo)
                    exit()
                else:
                    print("\033[31mRunning with normal user rights!\033[00m")
            else:
                if req_perm == True:
                    time.sleep(3)
                    run_sudo = (os.path.abspath(__file__))
                    run_sudo = "sudo " + run_sudo
                    os.system(run_sudo)
                    exit()
                else:
                    return sudo
    else:
        sudo = os.getuid()
        if sudo != 0:
            if verbose == True:
                print("\033[31mRunning with normal user rights!\033[00m")
            else:
                return sudo
        else:
            if verbose == True:
                if req_perm == True:
                    print("\033[31mRequesting normal user rights!\033[00m")
                    time.sleep(3)
                    run_sudo = (os.path.abspath(__file__))
                    run_sudo = "sudo " + run_sudo
                    os.system(run_sudo)
                    exit()
                else:
                    print("\033[31mRunning with normal user rights!\033[00m")
            else:
                if req_perm == True:
                    time.sleep(3)
                    run_sudo = (os.path.abspath(__file__))
                    os.system(run_sudo)
                    exit()
                else:
                    return sudo

def check_os_platform(verbose=True):
    system = platform

    if system == "darwin":
        if verbose == True:
            print("\033[31mMacOS detected!\033[00m")
            exit()
        else:
            return system
    elif system == "win32":
        if verbose == True:
            print("\033[31mWindows detected!\033[00m")
            exit()
        else:
            return system
    else:
        os.system("sudo grep -m 1 \"ID=\" /etc/os-release > /etc/phoenixthrush/os.txt")
        with open("/etc/phoenixthrush/os.txt") as f:
            content = f.read()

        if verbose == True:
            if content == "OS=arch":
                print("\033[31mArch based Distro detected!\033[00m")
            elif content == "OS=blackarch":
                print("\033[31mArch based Distro detected!\033[00m")
            elif content == "OS=debian":
                print("\033[31mDebian based Distro detected!\033[00m")
            elif content == "OS=ubuntu":
                print("\033[31mDebian based Distro detected!\033[00m")
            elif content == "OS=kali":
                print("\033[31mDebian based Distro detected!\033[00m")
            else:
                print("\033[31mCould not detect your distro!\033[00m")
                print("\033[31mExiting!\033[00m")
                user_exit()
        else:
            return content

def check_os_compatibility():
    os = check_os_platform()
    if os == "darwin":
        print("\033[31mThis Script doesn´t support MacOS yet!\033[00m")
    elif os == "win32":
        print("\033[31mThis Script doesn´t support Windows yet!\033[00m")
    else:
        pass

if __name__ == "__main__":
    check_os_compatibility()
    phoenixargs = phoenixparse()
    os.system("mkdir -p /etc/phoenixthrush")

    if phoenixargs.sudo == True:
        exit()
    if phoenixargs.update == True:
        exit()
    if phoenixargs.remove == True:
        exit()
    if phoenixargs.666 == True:
        random_cat()
        exit()
