#!/bin/bash
clear

if [ "$EUID" -ne 0 ]
  then echo -e "\e[31mPlease run this tool with admin rights!\e[0m"
  exit
fi


mkdir -p /usr/share/phoenixthrush/

rm /bin/phoenix
rm /usr/share/phoenixthrush/phoenix.sh
wget https://bit.ly/3m0JwFX && mv 3m0JwFX phoenix.sh && chmod +x phoenix.sh
mv phoenix.sh /usr/share/phoenixthrush/phoenix.sh

echo /usr/share/phoenixthrush/phoenix.sh > /bin/phoenix
chmod +x /bin/phoenix

clear 
echo -e "\e[31mInstalled!\e[0m"
echo -e "\e[31mYou can run the Script with: phoenix\e[0m"
exit