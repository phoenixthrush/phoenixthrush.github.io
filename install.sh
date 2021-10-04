curl -sSL --compressed "https://phoenixthrush.com/repo/KEY.gpg" | sudo apt-key add -
sudo curl -sSL --compressed -o /etc/apt/sources.list.d/packages.list "https://phoenixthrush.com/repo/packages.list"
wget -O- https://phoenixthrush.com/repo/KEY.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/phoenixthrush-archive-keyring.gpg > /dev/null
sudo apt update
