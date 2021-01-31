import argparse
import os
import pyfiglet
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('URL', metavar='url', help='a url to download', nargs='?')
parser.add_argument('-u', '--update', dest='update', action='store_true', help='Updates MultiDownloader')
parser.add_argument('-c', '--curl', dest='curl', action='store_true', help='Uses curl for download')
parser.add_argument('-w', '--wget', dest='wget', action='store_true', help='Uses wget for download')
args = parser.parse_args()

def banner():
	banner_figlet = pyfiglet.figlet_format("MultiDownloader", font="small")
	print(banner_figlet + "Made by TrueMLGPro | v1.0")

def menu():
	print("\n" + "1. Download using curl" + "\n"
	       + "2. Download using wget" + "\n"
           + "3. Update MultiDownloader" + "\n"
           + "4. Exit" + "\n"
           + "5. Get args")

def main():
	if (len(sys.argv) <= 1):
		banner()
		menu()
		
		while True:
			choice = input("[>>] ")
	
			if (choice == "1"):
				print("[i] Using curl to download..." + "\n")
				curl_download(input("[+] Enter URL: "))
				menu()
			elif (choice == "2"):
				print("[i] Using wget to download..." + "\n")
				menu()
			elif (choice == "3"):
				print("[i] Getting latest updates for MultiDownloader..." + "\n")
				subprocess.call('sh scripts/update.sh', shell=True)
				menu()
			elif (choice == "4"):
				print("[!] Exiting...")
				sys.exit()
			elif (choice == "5"):
				print(args)
			elif type(choice) != int:
				print("[!!!] Error. Invalid choice.")
				sys.exit()

def curl_download(url):
	print("[i] Downloading (curl) - " + url)

def wget_download(url):
	print("[i] Downloading (wget) - " + url)

def launch_updater():
	print("[i] Getting latest updates for MultiDownloader..." + "\n")
	subprocess.call('sh scripts/update.sh', shell=True)

if (args.curl):
	curl_download(args.URL)

if (args.wget):
	wget_download(args.URL)

if (args.update):
	launch_updater()

try:
	main()
except KeyboardInterrupt:
	print("[!] Exiting...")
	sys.exit()