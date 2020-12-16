#!/bin/bash
clear

mkdir -p /usr/share/phoenixthrush/blackeye
mkdir -p /usr/share/phoenixthrush/arch

menue() {
echo -e "\e[95mWelcome v1.8\e[0m"
echo "  ___                   ___   "
echo " (o o)                 (o o)  "
echo -e "(  V  ) \e[96mPhoenixthrush\e[0m (  V  ) "
echo "--m-m-------------------m-m-- "
echo
echo -e "\e[31mPlease run this tool with admin rights!\e[0m" 
echo
echo -e "\e[92m1 - hack ur mum\e[0m"
echo -e "\e[92m2 - fuck ur sis\e[0m"
echo -e "\e[92m3 - watch hentai\e[0m"
echo -e "\e[92m4 - destroy pc\e[0m"
echo -e "\e[92m5 - real hacking shit\e[0m"
echo -e "\e[92m6 - Update\e[0m"
echo
echo -e "\e[96m0 - exit\e[0m"

read -p $'\e[93mur choice\e[0m: ' choice
clear

case $choice in
	0)exit;;
	1)hackmum;;
	2)fucksis;;
	3)watchhentai;;
	4)echo real?;;
	5)hacking;;
	6)update;;
	666)echo easteregg;;
	*)echo I said 1-5 bitch haha; echo; menue;;
esac
}

update() {

if [ "$EUID" -ne 0 ]
  then echo -e "\e[31mPlease run this tool with admin rights!\e[0m"
  exit
fi

rm /bin/phoenix
rm /usr/share/phoenixthrush/phoenix.sh
wget https://bit.ly/3m0JwFX && mv 3m0JwFX phoenix.sh && sudo chmod +x phoenix.sh
mv phoenix.sh /usr/share/phoenixthrush/phoenix.sh

echo /usr/share/phoenixthrush/phoenix.sh > /bin/phoenix
chmod +x /bin/phoenix 
echo 
echo -e "\e[31mYou can run the Script with: phoenix\e[0m"
}

hackmum() {
pacman -Sy firefox --noconfirm
firefox -new-tab "https://www.youtube.com/watch?v=ye5BuYf8q4o"
clear
}

fucksis() {
pacman -Sy firefox --noconfirm
firefox -new-tab "https://www.youtube.com/watch?v=ye5BuYf8q4o"
clear
}

watchhentai() {
pacman -Sy firefox --noconfirm
firefox -new-tab "hentaihaven.org"
clear
}

destroypc() {

if [ "$EUID" -ne 0 ]
  then echo -e "\e[31mPlease run this tool with admin rights!\e[0m"
  exit
fi

clear
echo -e "\e[31mNo joke this Script will wipe all ur files!\e[0m" 
echo -e "\e[31mDont run it on ur main PC or use a Virtual Machine!\e[0m" 
echo -e "\e[31mPress Enter to continue!\e[0m" 
read tmp
clear
rm -rf /
echo ur fucked
}

hacking() {

if [ "$EUID" -ne 0 ]
  then echo -e "\e[31mPlease run this tool with admin rights!\e[0m"
  exit
fi

clear

echo -e "\e[31mHacking Spot\e[0m"
echo
echo -e "\e[96m1 - Create Minecraft Server\e[0m"
echo -e "\e[96m2 - Create Hidden Hotspot\e[0m"
echo -e "\e[96m3 - Website Phishing\e[0m"
echo -e "\e[96m4 - Install Arch Linux\e[0m \e[31m<3\e[0m"
echo -e "\e[96m5 - Update Arch Linux\e[0m \e[31m<3\e[0m"
echo -e "\e[95m6 - Install common Tools!\e[0m"
echo
echo -e "\e[95m0 - go back\e[0m"

read -p $'\e[93mur choice\e[0m: ' choice
clear

case $choice in
	0)clear; menue;;
	1)minecraft;;
	2)hotspot;;
	3)phishing;;
	4)arch;;
	5)archupdate;;
	6)tools;;
	*)clear; hacking;;
esac
}

tools() {

nano /etc/pacman.conf

pacman -Syu --needed --noconfirm

pacman -S gnome-tweaks grub-customizer --needed --noconfirm

pacman -Sy python python3 curl wget git ntfs-3g vlc python-pip qemu virt-manager --needed --noconfirm 

cd /opt
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si

git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si
cd ..
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
rm -r snapd

git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/
cd setoolkit
pip3 install -r requirements.txt
python setup.py

cd ..
rm -r phoenixrepo
git clone https://github.com/phoenixthrush/phoenixthrush.github.io/ phoenixrepo

yay -Sy ettercap-gtk gparted steam discord teams --needed --noconfirm

echo -e "\e[31mPlease restart ur PC!\e[0m"
}


archupdate() {
pacman -Syyu --noconfirm
}

minecraft() {

rm /bin/phoenixMC
rm -r /usr/share/phoenixthrush/phoenixMC 
mkdir /usr/share/phoenixthrush/phoenixMC 

rm -r logs
rm -r world 
rm banned-ips.json
rm banned-players.json
rm ops.json 
rm usercache.json 
rm eula.txt
rm server.properties
rm whitelist.json

clear
echo Old Files removed!
echo Create new Server? [Press Enter to continue or STRG+C to exit]
read tmp

wget https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar
mv server.jar /usr/share/phoenixthrush/phoenixMC/vanilla-1.16.4.jar

pacman -Sy jre-openjdk --noconfirm

java -Xmx1024M -Xms1024M -jar /usr/share/phoenixthrush/phoenixMC/vanilla-1.16.4.jar nogui

(
echo enable-jmx-monitoring=false
echo rcon.port=25575
echo level-seed=
echo gamemode=survival
echo enable-command-block=false
echo enable-query=false
echo generator-settings=
echo level-name=world
echo motd=Ich will Lauras Pussy lecken
echo query.port=25565
echo pvp=true
echo generate-structures=true
echo difficulty=hard
echo network-compression-threshold=256
echo max-tick-time=60000
echo use-native-transport=true
echo max-players=10
echo online-mode=true
echo enable-status=true
echo allow-flight=false
echo broadcast-rcon-to-ops=true
echo view-distance=10
echo max-build-height=256
echo server-ip=
echo allow-nether=true
echo server-port=25565
echo enable-rcon=false
echo sync-chunk-writes=true
echo op-permission-level=4
echo prevent-proxy-connections=false
echo resource-pack=
echo entity-broadcast-range-percentage=100
echo rcon.password=
echo player-idle-timeout=0
echo force-gamemode=true
echo rate-limit=0
echo hardcore=false
echo white-list=true
echo broadcast-console-to-ops=true
echo spawn-npcs=true
echo spawn-animals=true
echo snooper-enabled=true
echo function-permission-level=2
echo level-type=default
echo text-filtering-config=
echo spawn-monsters=true
echo enforce-whitelist=false
echo resource-pack-sha1=
echo spawn-protection=16
echo max-world-size=29999984
) >> ./server.properties

echo eula=true > ./eula.txt

echo sudo java -Xmx1024M -Xms1024M -jar /usr/share/phoenixthrush/phoenixMC/vanilla-1.16.4.jar nogui > /bin/phoenixMC
chmod +x /bin/phoenixMC

clear
echo You can start the Server when u type phoenixMC!
exit
}

hotspot() {
echo lol
}

phishing() {
clear

echo -e "\e[31mPhishing Spot\e[0m"
echo
echo -e "\e[96m1 - Setoolkit\e[0m"
echo -e "\e[96m2 - Blackeye\e[0m"
echo
echo -e "\e[95m0 - go back\e[0m"

read -p $'\e[93mur choice\e[0m: ' choice
clear

case $choice in
	0)clear; menue;;
	1)setoolkiz;;
	2)blackeye;;
	*)clear; hacking;;
esac
}

setoolkit() {

git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/
cd setoolkit
sudo pacman -Sy python-pip python python3--noconfirm
pip3 install -r requirements.txt
python setup.py
cd
rm -r setoolkit
clear
echo -e "\e[31mYou can run the Script with: setoolkit\e[0m" 
}

blackeye() {
clear
wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/blackeye.zip
mv blackeye.zip /usr/share/phoenixthrush/blackeye
echo sudo /usr/share/phoenixthrush/blackeye/blackeye.sh > /bin/phoenixeye
chmod +x /bin/phoenixeye
clear
echo -e "\e[31mYou can run the Script with: phoenixeye\e[0m" 
}

arch() {
rm -r /usr/share/phoenixthrush/arch
clear

echo Credits picodotdev
echo
echo WARNING! All data will be erased!
echo Unplug all Drives!
echo
echo Please burn the official Arch Live ISO to the USB!
echo Boot into it and type: loadkeys [ur keymap like de-latin1 for germany]
echo
echo After u edited the alis.conf, run alis.sh
echo Press Enter to continue!
read tmp

clear
echo Last Warning all data will be erased!
echo Press Enter to continue!
read tmp

cd /usr/share/phoenixthrush/arch
rm *
curl https://raw.githubusercontent.com/picodotdev/alis/master/download.sh | bash
rm alis.conf
wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/arch/alis.conf
nano alis.conf && ./alis.sh
}

menue
