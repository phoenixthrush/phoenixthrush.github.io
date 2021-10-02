curl -sSL --compressed "https://phoenixthrush.com/repo/KEY.gpg" | sudo apt-key add -
sudo curl -sSL --compressed -o /etc/apt/sources.list.d/packages.list "https://phoenixthrush.com/repo/packages.list"
sudo apt update
