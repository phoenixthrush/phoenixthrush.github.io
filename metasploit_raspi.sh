#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core libssl-dev libyaml-dev openssl autoconf libtool ncurses-dev bison curl wget postgresql postgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev -y 
sudo apt install ruby-dev -y
cd /opt
sudo git clone https://github.com/rapid7/metasploit-framework.git
cd metasploit-framework
sudo apt install git-core postgresql curl nmap gem libsqlite3-dev -y
sudo gem install wirble sqlite3 bundler
sudo gem install nokogiri
sudo gem install bundle
bundle install
./msfconsole
