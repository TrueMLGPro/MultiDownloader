import argparse
import os
import pyfiglet
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('URL', metavar='url', help='a url to download', nargs='?')
parser.add_argument('-u', '--update', action='store_true', help='Updates MultiDownloader')
parser.add_argument('-c', '--curl', action='store_true', help='Uses curl for download')
parser.add_argument('-w', '--wget', action='store_true', help='Uses wget for download')
parser.parse_args()

def banner():
	banner_figlet = pyfiglet.figlet_format("MultiDownloader", font="small")
	print(banner_figlet + "Made by TrueMLGPro | v1.0")

def menu():
	print("\n" + "1. Download using curl" + "\n"
	       + "2. Download using wget" + "\n"
           + "3. Update MultiDownloader" + "\n"
           + "4. Exit")

def main():
	banner()
	menu()
	while True:
		choice = input("[>>] ")
	
		if (choice == "1"):
			print("[i] Using curl to download..." + "\n")
			menu()
		elif (choice == "2"):
			print("[i] Using wget to download..." + "\n")
			menu()
		elif (choice == "3"):
			print("[i] Getting latest updates for MultiDownloader..." + "\n")
			subprocess.call('sh scripts/update.sh', shell=True)
			print("\n")
			menu()
		elif (choice == "4"):
			print("[!] Exiting...")
			sys.exit()
		elif type(choice) != int:
			print("[!!!] Error. Invalid choice.")
			sys.exit()

try:
	main()
except KeyboardInterrupt:
	print("[!] Exiting...")
	sys.exit()