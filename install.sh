#!/bin/bash
clear

sudo mkdir -p /usr/share/phoenixthrush/

sudo rm /bin/phoenix
sudo rm /usr/share/phoenixthrush/phoenix.sh
wget https://bit.ly/3m0JwFX && mv 3m0JwFX phoenix.sh && sudo chmod +x phoenix.sh
sudo mv phoenix.sh /usr/share/phoenixthrush/phoenix.sh

sudo echo /usr/share/phoenixthrush/phoenix.sh > /bin/phoenix
sudo chmod +x /bin/phoenix

clear 
echo -e "\e[31mInstalled!\e[0m"
echo -e "\e[31mYou can run the Script with: phoenix\e[0m"
exit
