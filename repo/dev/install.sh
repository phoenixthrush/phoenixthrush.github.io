clear
echo -e "\033[31m[*]\033[00m \033[96mStarting Installation!\033[00m"
sudo echo "idk something that prompts for admin that it looks nice lmao" >/dev/null 2>&1
echo -e "\n\033[31m[*]\033[00m \033[96mInstalling new keyring!\033[00m"
sudo curl -sSL https://phoenixthrush.com/repo/dev/ultrasecretcert.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/phoenixthrush-archive-keyring.gpg >/dev/null 2>&1
echo -e "\033[31m[*]\033[00m \033[96mAdding phoenixthrush to the apt source list!\033[00m\n"
sudo curl -sSL --compressed -o /etc/apt/sources.list.d/phoenixthrush-packages-dev.list "https://phoenixthrush.com/repo/dev/phoenixthrush-packages-dev.list" >/dev/null 2>&1
echo -e "\033[31m[*]\033[00m \033[96mUpdating sources!\033[00m"
sudo apt update >/dev/null 2>&1
echo -e "\033[31m[*]\033[00m \033[96mFinished! \033[00m\033[31m^^\033[00m\n"
