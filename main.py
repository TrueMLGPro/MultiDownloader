import os
import pyfiglet
import subprocess
import sys

def banner():
	banner_figlet = pyfiglet.figlet_format("MultiDownloader", font="small")
	print(banner_figlet)

def menu():
	print("1. Download using curl" + "\n"
	       + "2. Download using wget" + "\n"
           + "3. Update MultiDownloader" + "\n"
           + "4. Exit" + "\n")

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
			updater_executable = os.access('scripts/update.sh', os.X_OK)
			if (updater_executable):
				subprocess.call('scripts/update.sh', shell=True)
			else:
				os.chmod('scripts/update.sh', 0o777)
				subprocess.call('scripts/update.sh', shell=True)
			menu()
		elif (choice == "4"):
			print("[!] Exiting...")
			sys.exit()

try:
	main()
except KeyboardInterrupt:
	print("[!] Exiting...")
	sys.exit()