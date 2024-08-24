#code by blody
#instagram https://www.instagram.com/blody.sh
#github https://www.github.com/iamblody
#/usr/bin/python3

import socket
import os
from colorama import Fore, Style, init
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def usage():
    print(Fore.YELLOW + "Usage: python bps.py <target_host>")
    print(Fore.YELLOW + "Example: python bps.py 192.168.1.1")
    sys.exit()

def portSc(targetHost, targetPorts):
    for port in targetPorts:
        try:
            sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockt.settimeout(0.5)
            result = sockt.connect_ex((targetHost, port))

            if result == 0:
                print(Fore.GREEN + f"|{port} port is open|")
            else:
                print(Fore.RED + f"|{port} port is closed|")

            print(Fore.BLACK + "-------------------")
            sockt.close()

        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + "Try again.")
            break
        except socket.error:
            print(Fore.LIGHTMAGENTA_EX + "Disconnected.")
            break

# Banner
banner = Fore.CYAN + """
░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░  
blody         port         scanner                       
     
github https://github.com/iamblody            
"""

# Programın başında usage kontrolü
if len(sys.argv) != 2:
    usage()

clear()
print(banner)

# Hedef IP adresi
targetHost = sys.argv[1]

# Sabit port listesi
targetPort = [
    20, 21, 22, 23, 25, 53, 80, 110, 143, 139, 443, 445, 993, 995, 873, 115, 
    3306, 3389, 5900, 8080, 8443, 53, 161, 389, 636, 1723, 1900, 6667, 8000, 
    10000, 5000, 3306, 514
]

portSc(targetHost, targetPort)
