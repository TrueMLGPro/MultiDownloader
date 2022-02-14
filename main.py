# Copyright 2020 TrueMLGPro

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import pyfiglet
import subprocess
import sys

parser = argparse.ArgumentParser(add_help=False)
group_download = parser.add_argument_group('Download Tools')
group_download.add_argument('URL', metavar='url', help='a url to download', nargs='?')
group_download.add_argument('-c', '--curl', dest='curl', action='store_true', help='Uses curl for download')
group_download.add_argument('-w', '--wget', dest='wget', action='store_true', help='Uses wget for download')
group_download.add_argument('-H', '--httrack', dest='httrack', action='store_true', help='Uses httrack for mirroring')
group_download_args = parser.add_argument_group('Download Arguments')
group_download_args.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Makes output more detailed')
group_download_args.add_argument('-d', '--depth', dest='depth', help='Defines depth of mirror (httrack only)')
group_download_args.add_argument('-eD', '--ext-depth', dest='ext_depth', help='Defines depth of mirror for external links (httrack only)')
group_download_args.add_argument('-cN', '--conn-num', dest='conn_num', help='Defines a number of active connections during mirroring (httrack only)')
group_files = parser.add_argument_group('Files')
group_files.add_argument('-f', '--filename', dest='filename', help='Sets filename (or path) for file which is being downloaded')
group_misc = parser.add_argument_group('Misc')
group_misc.add_argument('-u', '--update', dest='update', action='store_true', help='Updates MultiDownloader')
group_misc.add_argument('-h', '--help', action='help', help='Shows this help message and exits')
args = parser.parse_args()

def banner():
	banner_figlet = pyfiglet.figlet_format("MultiDownloader", font="small")
	print(banner_figlet + "Made by TrueMLGPro | v1.0")

def menu():
	print("\n" + "1. Download using curl" + "\n"
	       + "2. Download using wget" + "\n"
           + "3. Mirror website using httrack" + "\n"
           + "4. Update MultiDownloader" + "\n"
           + "5. Exit" + "\n"
           + "6. Get args")

def main():
	if (len(sys.argv) <= 1):
		banner()
		menu()
		
		while True:
			choice = input("[>>] ")
	
			if (choice == "1"):
				print("[i] Using curl to download...")
				curl_download(input("[+] Enter URL: "),
					input("[+] Enter filename: "),
					input("[+] Verbose? (y/n): "))
				menu()
			elif (choice == "2"):
				print("[i] Using wget to download...")
				wget_download(input("[+] Enter URL: "),
					input("[+] Enter filename: "),
					input("[+] Verbose? (y/n): "))
				menu()
			elif (choice == "3"):
				print("[i] Using httrack to mirror...")
				httrack_download(input("[+] Enter URL: "),
					input("[+] Enter project path for mirror: "),
					input("[+] Enter depth level: "),
					input("[+] Enter external links depth level: "),
					input("[+] Enter number of connections: "),
					input("[+] Verbose? (y/n): "))
			elif (choice == "4"):
				print("[i] Getting latest updates for MultiDownloader..." + "\n")
				subprocess.call('sh scripts/update.sh', shell=True)
				menu()
			elif (choice == "5"):
				print("[!] Exiting...")
				sys.exit()
			elif (choice == "6"):
				print(args)
			elif type(choice) != int:
				print("[!!!] Invalid choice. Exiting...")
				sys.exit()

def curl_download(url, filename, verbose=None):
	print("[i] Downloading using curl - " + url + " with filename: " + filename)
	if (verbose == "y"):
		subprocess.call(f"curl -L -O {filename} -v {url}", shell=True)
	elif (verbose == "n"):
		subprocess.call(f"curl -L -O {filename} {url}", shell=True)
	else:
		subprocess.call(f"curl -L -O {filename} {url}", shell=True)

def wget_download(url, filename, verbose=None):
	print("[i] Downloading using wget - " + url + " with filename: " + filename + "\n" + ("Verbose: ") + str(verbose))
	if (verbose == "y"):	
		subprocess.call(f"wget -O {filename} -v {url}", shell=True)
	elif (verbose == "n"):
		subprocess.call(f"wget -O {filename} {url}", shell=True)
	else:
		subprocess.call(f"wget -O {filename} {url}", shell=True)

def httrack_download(url, path, mirror_depth, ext_links_depth, conn_num, verbose=None):
	print("[i] Cloning using httrack - " + url + " on path: " + path)
	subprocess.call(f"httrack {url} -O {path} -r{mirror_depth} -%e{ext_links_depth} -c{conn_num}", shell=True)

def launch_updater():
	print("[i] Getting latest updates for MultiDownloader..." + "\n")
	subprocess.call('sh scripts/update.sh', shell=True)

if (args.curl):
	if (args.verbose):
		curl_download(args.URL, args.filename, args.verbose)
	else:
		curl_download(args.URL, args.filename)

if (args.wget):
	if (args.verbose):
		wget_download(args.URL, args.filename, args.verbose)
	else:
		wget_download(args.URL, args.filename)

if (args.httrack):
	if (args.verbose):
		httrack_download(args.URL, args.filename, args.depth, args.ext_depth, args.conn_num, args.verbose)
	else:
		httrack_download(args.URL, args.filename, args.depth, args.ext_depth, args.conn_num)

if (args.update):
	launch_updater()

try:
	main()
except KeyboardInterrupt:
	print("[!] Exiting...")
	sys.exit()