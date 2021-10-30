# Create your own debian packages and host your own ppa

This is an example! </br>
Please change the email adress and vars also the links!


## Create debian packages

```shell
mkdir nezuko
mkdir nezuko/DEBIAN
vi nezuko/DEBIAN/control

# sample control file from linuxconfig.org:

# Package: linuxconfig
# Version: 1.0
# Section: custom
# Priority: optional
# Architecture: all
# Essential: no
# Installed-Size: 1024
# Maintainer: linuxconfig.org
# Description: Print linuxconfig.org on the screen

mkdir -p nezuko/usr/bin/
# copy your deb files to nezuko/usr/bin

dpkg-deb --build nezuko

# now rename your nezuko.deb to something like nezuko_0.0.1-1_all.deb
```

## Create new repo

Create a folder and cd into it and copy your deb files to that dir!

```shell
EMAIL="contact@phoenixthrush.com"

sudo apt install gnupg
gpg --full-gen-key
gpg --export-secret-keys "${EMAIL}" > my-private-key.asc
gpg --import my-private-key.asc
gpg --armor --export "${EMAIL}" > ./ultrasecretcert.gpg

dpkg-scanpackages --multiversion . > Packages
gzip -k -f Packages
apt-ftparchive release . > Release

gpg --default-key "${EMAIL}" -abs -o - Release > Release.gpg
gpg --default-key "${EMAIL}" --clearsign -o - Release > InRelease

echo "deb [signed-by=/usr/share/keyrings/phoenixthrush-archive-keyring.gpg] https://phoenixthrush.com/repo/stable ./" > phoenixthrush-packages.list 
```

## Add new packages

```shell
EMAIL="contact@phoenixthrush.com"

dpkg-scanpackages --multiversion . > Packages
gzip -k -f Packages
apt-ftparchive release . > Release

gpg --default-key "${EMAIL}" -abs -o - Release > Release.gpg
gpg --default-key "${EMAIL}" --clearsign -o - Release > InRelease
```
## Give that commands to your friends

```shell
sudo curl -sSL https://phoenixthrush.com/repo/stable/ultrasecretcert.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/phoenixthrush-archive-keyring.gpg >/dev/null 2>&1
sudo curl -sSL --compressed -o /etc/apt/sources.list.d/phoenixthrush-packages.list "https://phoenixthrush.com/repo/stable/phoenixthrush-packages.list" >/dev/null 2>&1
sudo apt update >/dev/null 2>&1
```
