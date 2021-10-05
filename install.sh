sudo apt update
sudo apt install curl -y
sudo curl -sSL https://phoenixthrush.com/repo/KEY.gpg > KEY.gpg
sudo cat KEY.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/phoenixthrush-archive-keyring.gpg
sudo curl -sSL --compressed -o /etc/apt/sources.list.d/packages.list "https://phoenixthrush.com/repo/packages.list"
sudo rm KEY.gpg
clear
sudo apt update
