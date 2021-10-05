sudo wget -O- https://phoenixthrush.com/repo/KEY.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/phoenixthrush-archive-keyring.gpg
sudo curl -sSL --compressed -o /etc/apt/sources.list.d/packages.list "https://phoenixthrush.com/repo/packages.list"
sudo apt update
