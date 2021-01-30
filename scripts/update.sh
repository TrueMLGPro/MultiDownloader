#!/bin/bash
REQUIRED_PKG="git"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG | grep "install ok installed")
echo "[1/2] [i] Checking for $REQUIRED_PKG: $PKG_OK"
if [ "" = "$PKG_OK" ]; then
  echo "[!] No $REQUIRED_PKG found. Setting up $REQUIRED_PKG..."
  apt --yes install $REQUIRED_PKG
fi

echo "[2/2] [i] Pulling latest changes from repo..."
git pull origin master
echo "[i] Done."