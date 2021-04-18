#!/usr/bin/env python3
import os
import time
import shutil
import subprocess
import random

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
        print("\033[31mYour System is based on Debian right?\033[00m")
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
            os.system("sudo pacman -Syu " + package + " --needed --noconfirm")
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

def menue_check_sudo_status():
    if get_sudo_info() == True:
        print("\033[96mYou have \033[31msudo\033[96m rights!\033[00m")
    else:
        print("\033[96mYou have normal user rights!\033[00m")

def run_sudo_menue():
    clear()
    check_sudo()
    current_path = os.path.abspath(__file__)
    current_path = "sudo python3 " + current_path
    os.system(current_path)
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
    else:
        print()
        print("\033[31mError sorry buddy!\033[00m")
    exit()

def asian_cat_1():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
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

def asian_cat_2():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
    print(r"""
   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
    """)

def asian_cat_3():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
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

def asian_cat_4():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
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

def asian_cat_5():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
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

def asian_cat_6():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
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

def asian_cat_7():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
    print(r"""
        _,'|             _.-''``-...___..--';)
       /_ \'.      __..-' ,      ,--...--'''
      <\    .`--'''       `     /'
       `-';'               ;   ; ;
 __...--''     ___...--_..'  .;.'
(,__....----'''       (,..--''   *asian meow*
    """)

def asian_cat_8():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
    print(r"""
(:`--..___...-''``-._             |`._
  ```--...--.      . `-..__      .`/ _\  
            `\     '       ```--`.    />
            : :   :               `:`-'
             `.:.  `.._--...___     ``--...__      
                ``--..,)       ```----....__,) *bug*
    """)

def asian_cat_9():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
    print(r"""
              __..--''``---....___   _..._    __
    /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
   ///_.-' _..--.'_    \                    `( ) ) // //
   / (_..-' // (< _     ;_..__               ; `' / ///
    / // // //  `-._,_)' // / ``--...____..-' /// / //
        """)

def asian_cat_10():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[00m")
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

def menue():
    clear()
    print("\033[95mWelcome to Phoenixsploit v.3.7\033[00m")
    menue_check_sudo_status()
    print("\033[95m  ___                   ___   ")
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
        install_and_update()
        exit()
    elif choice == 5:
        remove_phoenixsploit()
        exit()
    elif choice == 6:
        run_sudo_menue()
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
    clear()
    check_not_sudo()
    if check_package("firefox") == True:
        print()
        print("\033[32mOkay buddy let me help you!")
        os.system("firefox -new -tab ´https://hentaihaven.xxx´")
    else:
        print()
        print("\033[31mCouldn´t install a program!\033[00m")

def destroy_pc():
    clear()
    print("Destroyed!")
    print("Just kidding")

def second_menue():
    clear()
    menue_check_sudo_status()
    check_os()
    hack_menue()
    user_exit()

def install_and_update():
    clear()
    check_sudo()
    print()
    print("\033[31mChecking dependency\033[00m")
    print()
    check_package("wget")
    check_package("python3")
    if os.path.exists("/etc/phoenixthrush/update"):
        print()
        print("\033[96mOld files found!\033[00m")
        print("\033[96mDeleting old files\033[00m")
        os.system("sudo rm -rf /etc/phoenixthrush/update")
        os.system("sudo rm /etc/phoenixthrush/phoenixsploit")
        print("\033[96mDeleted old files!\033[00m")
        install_and_update_2()
        exit()
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
    x.write("clear && sudo python3 /etc/phoenixthrush/update/install.py")
    os.system("sudo chmod +x /bin/phoenixupdate")
    os.system("sudo chmod 777 /bin/phoenixupdate")

    os.system("sudo python3 /etc/phoenixthrush/update/install.py")
    print()

def remove_phoenixsploit():
    clear()
    check_sudo()
    print()
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

    if os.path.exists("/bin/phoenixMC"):
        os.system("sudo rm /bin/phoenixMC")
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
    print("\033[96m1 - Create a Minecraft-Server    \033[31m[Beta!]\033[00m")
    print("\033[96m2 - Create a hidden hotspot      \033[31m[Coming soon!]\033[00m")
    print("\033[96m3 - Website Phishing (blackeye)\033[00m")
    print("\033[96m4 - Install common tools\033[00m")
    print("\033[96m5 - Update Linux\033[00m")
    print("\033[96m6 - Install Arch Linux\033[00m \033[31m<3\033[00m")
    print("\033[96m7 - Base64 Encoder/ Decoder\033[00m \033[31m<3\033[00m")
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
    elif choice == 7:
        base64()
        exit()
    elif choice == 666:
        random_cat()
        exit()
    elif choice == 0:
        menue()
        exit()
    else:
        second_menue()
        exit()

def minecraft_server():
    clear()
    check_sudo()
    print()
    check_package("nano")
    check_package("default-jdk")
    check_package("default-jre")
    print()
    if os.path.exists("/etc/phoenixthrush/phoenixMC"):
        choice = input("\033[96mDo you want to overwrite or remove the old Server files? [overwrite|uninstall] \033[00m")
        if choice == "overwrite":
            minecraft_server_step_1()
            exit()
        elif choice == "uninstall":
            os.system("sudo rm -rf /etc/phoenixthrush/phoenixMC")
            os.system("sudo rm /bin/phoenixMC")
            print("\033[31mRemoved Server!\033[00m")
            print()
        else:
            minecraft_server()
            exit()
    else:
        minecraft_server_step_1()
        exit()


def minecraft_server_step_1():
    clear()
    print("\033[31mStarting Minecraft Server installation!\033[00m")
    print()
    print("\033[31mChecking files\033[00m")
    if os.path.exists("/bin/phoenixMC"):
        print("\033[31mFound old bin files!\033[00m")
        choice = input("\033[96mDo you want to remove them? [y|n] \033[00m")
        print()
        if choice == "y":
            print("\033[31mRemoving Files!\033[00m")
            os.system("sudo rm /bin/phoenixMC")
            print("\033[31mRemoved Files!\033[00m")
        elif choice == "n":
            print("\033[31mExiting Minecraft Installer!\033[00m")
            time.sleep(10)
            user_exit()
            exit()
        else:
            minecraft_server_step_1()
            exit()
    else:
        print("\033[96mNo old bin files found!\033[00m")
    if os.path.exists("/etc/phoenixthrush/phoenixMC"):
        print()
        print("\033[31mFound old Server files!\033[00m")
        choice = input("\033[96mDo you want to remove them? [y|n] \033[00m")
        if choice == "y":
            print()
            print("\033[31mRemoving Files!\033[00m")
            os.system("sudo rm -rf /etc/phoenixthrush/phoenixMC")
            print("\033[31mRemoved Files!\033[00m")
            minecraft_server_step_2()
            exit()
        elif choice == "n":
            print("\033[31mExiting Minecraft Installer!\033[00m")
            time.sleep(5)
            user_exit()
            exit()
        else:
            minecraft_server_step_1()
            exit()

    else:
        print("\033[96mNo old Server files found!\033[00m")
        print()
        print("\033[31mChecked files!\033[00m")
        print("\033[31mStarting configs!\033[00m")
        minecraft_server_step_2()
        exit()

def minecraft_server_step_2():
    time.sleep(3)
    clear()
    print("\033[96mSupport for forge Minecraft Server coming soon!\033[00m")
    print("\033[96mDownloading Minecraft Server Vanilla jar\033[00m")
    print("\033[96mVersion 1.16.5\033[00m")
    print()

    os.system("sudo mkdir -p /etc/phoenixthrush/phoenixMC")
    os.system("sudo chmod 777 /etc/phoenixthrush/phoenixMC")
    os.system("wget https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar")
    print("\033[96mDownloaded jar\033[00m")

    current_dir = os.getcwd()
    current_dir += "/server.jar"
    original = current_dir
    target = "/etc/phoenixthrush/phoenixMC/server.jar"
    shutil.move(original, target)

    print("\033[96mMoved jar to /etc/phoenixthrush/phoenixMC\033[00m")
    minecraft_server_step_3()
    exit()

def minecraft_server_step_3():
    print()
    try:
        ram = int(input("\033[31mHow much GB ram do you want for your minecraft server? [1,2,3...,16] \033[00m"))
    except ValueError:
        print("\033[31mError wrong input!\033[00m")
        minecraft_server_step_3()
        exit()

    if ram < 17 and not ram == 0:
        print("\033[31mSetting ram to " + str(ram) + "GB\033[00m")
    else:
        print("\033[31mError wrong input!\033[00m")
        minecraft_server_step_3()
        exit()

    phoenix_mc_start_command = "cd /etc/phoenixthrush/phoenixMC/ && java -Xmx" + str(ram) + "G -Xms" + str(ram) + "G -jar ./server.jar nogui"
    print()
    print("\033[96mUsing " + phoenix_mc_start_command + " as start trigger!\033[00m")

    os.system(phoenix_mc_start_command)

    java_start = str(phoenix_mc_start_command)
    java_start1 = "clear && " + java_start

    x = open("/bin/phoenixMC", "x")
    x.write(java_start1)
    os.system("sudo chmod +x /bin/phoenixMC")
    os.system("sudo chmod 777 /bin/phoenixMC")
    minecraft_server_step_4()

def minecraft_server_step_4():
    print()
    choice = input("\033[96mDo you want to manually edit settings? (recommended) [y|n] \033[00m")
    if choice == "y":
        minecraft_server_config_manually()
    elif choice == "n":
        minecraft_server_config()
        exit()
    else:
        minecraft_server_step_4()
        exit()

def minecraft_server_config():
    os.system("nano /etc/phoenixMC/eula.txt")
    minecraft_eula()
    print("\033[31mYou can start the Server with phoenixMC\033[00m")
    exit()

def minecraft_server_config_manually():
    os.system("nano /etc/phoenixMC/server.properties")
    os.system("nano /etc/phoenixMC/eula.txt")
    minecraft_eula()
    print("\033[31mYou can start the Server with phoenixMC\033[00m")
    exit()

def minecraft_eula():
    x = open("/etc/phoenixthrush/phoenixMC/eula.txt", "w")
    x.write("eula=true")

def hidden_hotspot():
    print("Coming soon!")
    input("If you press enter it will start with a non finished script!")
    input("Last warning!")
    input("Ok buddy")

    clear()
    check_sudo()
    print()
    print("\033[96mChecking for requests!\033[00m")
    check_package("hostapd")
    check_package("udhcpd")
    print()
    os.system("sudo iw phy phy0 interface add new1 type __ap")
    os.system("ifconfig hotspot 192.168.3.1 up")
    hostapd = open("/etc/phoenixthrush/hostapd.conf", "x")
    hostapd.write("interface=wlan0")
    hostapd.close()
    hostapd1 = open("/etc/phoenixthrush/hostapd.conf", "a")
    hostapd1.write("\ndriver=nl80211)")
    hostapd1.write("\nssid=phoenix")
    hostapd1.write("\nchannel=7")
    hostapd1.write("\nhw_mode=g")
    hostapd1.write("\nwme_enabled=1")
    hostapd1.write("\nmacaddr_acl=0")
    hostapd1.write("\nauth_algs=1")
    hostapd1.write("\nignore_broadcast_ssid=1")
    hostapd1.write("\nwpa=3")
    hostapd1.write("\nwpa_passphrase=phoenixthrush")
    hostapd1.write("\nwpa_key_mgmt=WPA-PSK")
    hostapd1.write("\nwpa_pairwise=TKIP")
    hostapd1.write("\nrsn_pairwise=CCMP")
    #os.system("cd /etc/phoenixthrush && sudo hostapd hostapd.conf")
    hostapd1.close()
    udhcpd = open("/etc/udhcpd.conf", "w")
    udhcpd.write("start 192.168.3.2")
    udhcpd.write("\nend 192.168.3.254")
    udhcpd.write("\ninterface hotspot")
    udhcpd.write("\nopt dns 1.1.1.1 1.0.0.1")
    udhcpd.write("\noption subnet 255.255.255.0")
    udhcpd.write("\nopt router 192.168.2.118")
    udhcpd.write("\noption domain local")
    udhcpd.write("\noption lease 864000")
    udhcpd.close()
    #os.system("sudo udhcd -f")

    print("Please open up 2 terminals and type \"sudo udhcd -f\" and on the other one \"cd /etc/phoenixthrush && sudo hostapd hostapd.conf\"")

    os.system("sudo echo \"1\" > /proc/sys/net/ipv4/ip_forward")
    os.system("sudo iptables --table nat --append POSTROUTING --out-interface wlo1 -j MASQUERADE")
    os.system("sudo iptables --append FORWARD --in-interface hotspot -j ACCEPT")

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
    check_sudo()
    print()
    print("\033[31mInstalling common tools!\033[00m")
    print()
    check_package("vim")
    check_package("nano")
    check_package("neofetch")
    check_package("htop")
    check_package("default-jdk")
    check_package("default-jre")
    check_package("python3")
    check_package("python3-pip")
    print()
    print("\033[31mCommon tools are installed!\033[00m")
    print()

def update_linux():
    clear()
    check_sudo()
    print()
    print("\033[31mUpdating Linux!\033[00m")
    print()
    if get_os_info() == "Debian":
        os.system("apt update -y")
        os.system("sudo apt full-upgrade -y")
        os.system("sudo apt autoremove -y")

    print()
    print("\033[31mUpdated Linux!\033[00m")
    print()

def arch_install():
    clear()
    check_sudo()
    print()
    check_package("nano")
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

def base64():
    clear()
    check_sudo()
    if os.path.exists("/etc/phoenixthrush/phoenix_base64.py"):
        base64_1()
        exit()
    else:
        print("\033[31mDidn´t found installed base64 file!\033[00m")
        print()
        print("\033[96mTrying to download it!\033[00m")
        print()
        os.system("wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/python/base64.py")
        print("\033[96mDownloaded it!\033[00m")
        print("\033[96mMoving file to /etc/phoenixthrush/phoenix_base64.py!\033[00m")
        print()
        current_dir1 = os.getcwd()
        current_dir1 += "/base64.py"
        original1 = current_dir1
        target1 = "/etc/phoenixthrush/phoenix_base64.py"
        shutil.move(original1, target1)
        time.sleep(3)
        base64_1()
        exit()

def base64_1():
    import phoenix_base64
    phoenix_base64.menue()

if __name__ == "__main__":
    menue()
