mkdir -p /etc/phoenixthrush

rm -f /bin/phoenix
rm -f /etc/phoenixthrush/phoenix.sh

cd /etc/phoenixthrush
wget https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/linux/phoenix/phoenix.sh
sudo chmod +x phoenix.sh

echo /etc/phoenixthrush/phoenix.sh > /bin/phoenixthrush
sudo chmod +x /bin/phoenix

echo -e "\e[31mUpdated!\e[0m"
echo -e "\e[31mYou can run the Script with: phoenix\e[0m"
