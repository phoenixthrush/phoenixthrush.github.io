sudo curl -sSL https://phoenixthrush.com/repo/KEY.gpg > key.gpg

sudo apt-key add ./key.gpg
sudo mv /etc/apt/trusted.gpg /etc/apt/trusted.gpg.d/phoenixthrush-archive-keyring.gpg

sudo apt-key add /etc/apt/trusted.gpg.d/phoenixthrush-archive-keyring.gpg
sudo curl -sSL --compressed -o /etc/apt/sources.list.d/packages.list "https://phoenixthrush.com/repo/packages.list"

sudo curl -sSL https://phoenixthrush.com/repo/KEY.gpg > phoenixthrush-archive-keyring.gpg

sudo gpg --dearmor ./key.gpg > dearmor.gpg 
sudo mv dearmor.gpg /usr/share/keyrings/phoenixthrush-archive-keyring.gpg

sudo apt update
