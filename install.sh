#!/bin/bash
echo "$(tput -T xterm setaf 2)[1/7] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Starting installation. Checking for package updates..."
apt update --yes
apt upgrade --yes
REQUIRED_PKG1="git"
PKG_OK1=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG1 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[2/7] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG1: $PKG_OK1"
if [ "" = "$PKG_OK1" ]; then
  echo "[!] No $REQUIRED_PKG1 found. Setting up $REQUIRED_PKG1."
  apt --yes install $REQUIRED_PKG1
fi
REQUIRED_PKG2="python3"
PKG_OK2=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG2 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[3/7] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG2: $PKG_OK2"
if [ "" = "$PKG_OK2" ]; then
  echo "[!] No $REQUIRED_PKG2 found. Setting up $REQUIRED_PKG2."
  apt --yes install $REQUIRED_PKG2
fi
REQUIRED_PKG3="curl"
PKG_OK3=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG3 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[4/7] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG3: $PKG_OK3"
if [ "" = "$PKG_OK3" ]; then
  echo "[!] No $REQUIRED_PKG3 found. Setting up $REQUIRED_PKG3."
  apt --yes install $REQUIRED_PKG3
fi
REQUIRED_PKG4="wget"
PKG_OK4=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG4 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[5/7] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG4: $PKG_OK4"
if [ "" = "$PKG_OK4" ]; then
  echo "[!] No $REQUIRED_PKG4 found. Setting up $REQUIRED_PKG4."
  apt --yes install $REQUIRED_PKG4
fi
REQUIRED_PKG5="httrack"
PKG_OK5=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG5 | grep "install ok installed")
echo "$(tput -T xterm setaf 2)[6/7] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Checking for $REQUIRED_PKG5: $PKG_OK5"
if [ "" = "$PKG_OK5" ]; then
  echo "[!] No $REQUIRED_PKG5 found. Setting up $REQUIRED_PKG5."
  apt --yes install $REQUIRED_PKG5
fi
echo "$(tput -T xterm setaf 2)[7/7] $(tput -T xterm setaf 4)[i] $(tput -T xterm sgr0)Installing requirements..."
pip3 install -r REQUIREMENTS.txt
echo "$(tput -T xterm setaf 2)[✓] Done.$(tput -T xterm sgr0)"
