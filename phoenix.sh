#!/bin/bash
clear

if [ "$EUID" -ne 0 ]
  then echo -e "\e[31mPlease run this tool with admin rights!\e[0m"
  exit
fi

mkdir -p /usr/share/phoenixthrush
mkdir -p /usr/share/phoenixthrush/blackeye
mkdir -p /usr/share/phoenixthrush/arch

menue() {
echo -e "\e[95mWelcome v1.6\e[0m"
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
echo
echo -e "\e[96m0 - exit\e[0m"

read -p $'\e[93mur choice\e[0m: ' choice
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

echo -e "\e[31mHacking Spot\e[0m"
echo
echo -e "\e[96m1 - Create Minecraft Server\e[0m"
echo -e "\e[96m2 - Create Hidden Hotspot\e[0m"
echo -e "\e[96m3 - Website Phishing\e[0m"
echo -e "\e[96m4 - Install Arch Linux\e[0m \e[31m<3\e[0m"
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
	*)clear; hacking;;
esac
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

cd /usr/share/phoenixthrush/arch
rm *
curl https://raw.githubusercontent.com/picodotdev/alis/master/download.sh | bash
rm alis.conf
wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/arch/alis.conf
nano alis.conf && ./alis.sh
}

menue
