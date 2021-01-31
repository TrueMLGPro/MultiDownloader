#!/bin/bash
echo "$(tput -T xterm setaf 2)[1/6] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Starting installation. Checking for package updates..."
sudo apt update --yes
sudo apt upgrade --yes
REQUIRED_PKG1="git"
PKG_OK1=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG1 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[2/6] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG1: $PKG_OK1"
if [ "" = "$PKG_OK1" ]; then
  echo "[!] No $REQUIRED_PKG1 found. Setting up $REQUIRED_PKG1."
  sudo apt --yes install $REQUIRED_PKG1
fi
REQUIRED_PKG2="python"
PKG_OK2=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG2 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[3/6] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG2: $PKG_OK2"
if [ "" = "$PKG_OK2" ]; then
  echo "[!] No $REQUIRED_PKG2 found. Setting up $REQUIRED_PKG2."
  sudo apt --yes install $REQUIRED_PKG2
fi
REQUIRED_PKG3="curl"
PKG_OK3=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG3 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[4/6] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG3: $PKG_OK3"
if [ "" = "$PKG_OK3" ]; then
  echo "[!] No $REQUIRED_PKG3 found. Setting up $REQUIRED_PKG3."
  sudo apt --yes install $REQUIRED_PKG3
fi
REQUIRED_PKG4="wget"
PKG_OK4=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG4 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[5/6] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG4: $PKG_OK4"
if [ "" = "$PKG_OK4" ]; then
  echo "[!] No $REQUIRED_PKG4 found. Setting up $REQUIRED_PKG4."
  sudo apt --yes install $REQUIRED_PKG4
fi
echo "$(tput -T xterm setaf 2)[6/6] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Installing requirements..."
pip3 install -r REQUIREMENTS.txt
echo "$(tput -T xterm setaf 2)[i] Done.$(tput -T sgr0)"
