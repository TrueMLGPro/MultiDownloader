#!/bin/bash
REQUIRED_PKG="git"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG | grep "install ok installed")
echo "$(tput setaf 2)[1/2] $(tput setaf 4)[i] $(tput sgr0)Checking for $REQUIRED_PKG: $PKG_OK"
if [ "" = "$PKG_OK" ]; then
  echo "[!] No $REQUIRED_PKG found. Setting up $REQUIRED_PKG..."
  apt --yes install $REQUIRED_PKG
fi
echo "$(tput setaf 2)[2/2] $(tput setaf 4)[i] $(tput sgr0)Pulling latest changes from repo..."
git pull origin master
echo "$(tput setaf 2)[i] Done.$(tput sgr0)"