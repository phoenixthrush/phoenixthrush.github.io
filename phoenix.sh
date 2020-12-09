#!/bin/bash
clear

mkdir -p ~/phoenixthrush
mkdir -p ~/phoenixthrush/blackeye
mkdir -p ~/phoenixthrush/arch
mkdir -p ~/phoenixthrush/minecraft
mkdir -p ~/phoenixthrush/minecraft/server

menue() {
echo Welcome
echo "  ___                   ___   "
echo " (o o)                 (o o)  "
echo "(  V  ) Phoenixthrush (  V  ) "
echo "--m-m-------------------m-m-- "

echo
echo 1 - hack ur mom
echo 2 - fuck ur sis
echo 3 - watch hentai
echo 4 - destroy pc
echo 5 - real hacking shit
echo
echo 0 - exit

echo
echo Choose:
read choice
clear

case $choice in
	0)exit;;
	1)echo hacking mum;;
	2)echo dont do it buddy;;
	3)echo uh okay;;
	4)echo real?;;
	5)hacking;;
	666)echo easteregg;;
	*)echo I said 1-5 bitch haha; echo; menue;;
esac
}

hacking() {
clear

echo Hacking Spot
echo 1 - Minecraft Server
echo 2 - WIFI Hotspot
echo 3 - Website Phishing
echo 4 - Install Arch Linux \<3
echo
echo 0 - Menue

echo Choose:
read choice
clear

case $choice in
	0)clear; menue;;
	1)minecraft;;
	2)hotspot;;
	3)phishing;;
	4)arch;;
	*)clear; hacking;;
esac
}

minecraft() {
wget https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar ∼/phoenixthrush/minecraft/vanilla-1.16.4.jar
}

hotspot() {
echo lol
}

phishing() {
echo lol
}

arch() {
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

cd ~/phoenixthrush/arch/
curl https://raw.githubusercontent.com/picodotdev/alis/master/download.sh | bash
rm alis.conf
wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/arch/alis.conf
nano alis.conf && ./alis.sh
}

menue
