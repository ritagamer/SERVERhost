#Libraries
from colorama import Fore, Back
import socket
import subprocess
import ipaddress
import sys
import time
import pyfiglet
import json

# Variables
option=[1,2,3,4,5]

# Port Verification
def is_port_available(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            return False
        except OSError:
            return True

# IP verification
def is_valid_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

with open('date.json', 'r') as f:
    # Load JSON data from the file
    data = json.load(f)

def save_json():
    with open('date.json', "w") as f:
        json.dump(data, f)

# Main
try:
    def main(host, port):
        while True:
            host = data["configuration"]["automatic"]["host"]
            port = data["configuration"]["automatic"]["port"]
            subprocess.run("cls", shell=True)
            print(pyfiglet.figlet_format("SEVERhost"))
            print("_" * 65)
            print(f'\n[1] Automatic ({host}:{port})\n[2] Manual (custom IP and Port)\n[3] Last session\n[4] Settings\n[5] Exit')
            print("_" * 65)
            try:
                put = int(input("option: "))
            except KeyboardInterrupt:
                print("\nProgram interrupted by user")
                sys.exit()
            except ValueError:
                print(f"{Fore.RED}[!]{Fore.RESET} Error: Invalid input. Please enter a valid number.")
                time.sleep(2)
                continue

            if put == option[0]:
                session="automatic"
                host = data["configuration"]["automatic"]["host"]
                port = data["configuration"]["automatic"]["port"]
                session = data["configuration"]["session"]["id"]
                save_json()
                break
            elif put == option[1]:
                subprocess.run("cls", shell=True)
                print("\n" + pyfiglet.figlet_format("SEVERhost\n"))

                try:
                    host_input = str(input("HOST: "))
                except KeyboardInterrupt:
                    print("\nProgram interrupted by user")
                    sys.exit()

                if host_input.lower() == "localhost" or is_valid_ip(host_input):
                    host = host_input
                else:
                    print(f"{Fore.RED}[!]{Fore.RESET} Error: Invalid IP address or not \"localhost\"")
                    time.sleep(2)
                    continue

                try:
                    port = int(input("PORT: "))
                except KeyboardInterrupt:
                    print("\nProgram interrupted by user")
                    sys.exit()
                except ValueError:
                    print(f"{Fore.RED}[!]{Fore.RESET} Error: Port is not a valid number")
                    time.sleep(2)
                    continue

                if not is_port_available(host, port):
                    print(f"{Fore.RED}[!]{Fore.RESET} Error: The Port is occupied")
                    time.sleep(2)
                    continue

            elif put == option[2]:
                subprocess.run("cls", shell=True)
                break
            elif put == option[3]:
                subprocess.run("cls", shell=True)
                print(pyfiglet.figlet_format("SEVERsettings"))
                print("_" * 65)
                print('\n[1] Change automatic (localhost and 55555 Port)\n[2] Exit')
                print("_" * 65)
                try:
                    setting = int(input("option: "))
                except KeyboardInterrupt:
                    print("\nProgram interrupted by user")
                    sys.exit()
                except ValueError:
                    print(f"{Fore.RED}[!]{Fore.RESET} Error: Invalid input. Please enter a valid number.")
                    time.sleep(2)
                    continue
                if setting == option[0]:
                    subprocess.run("cls", shell=True)
                    print("\n" + pyfiglet.figlet_format("SEVERsettings\n"))

                    try:
                        host = str(input("HOST: "))
                    except KeyboardInterrupt:
                        print("\nProgram interrupted by user")
                        sys.exit()

                    if host.lower() == "localhost" or is_valid_ip(host):
                        host = "localhost" if host.lower() == "localhost" else host
                    else:
                        print(f"{Fore.RED}[!]{Fore.RESET} Error: Invalid IP address or not \"localhost\"")
                        time.sleep(2)
                        continue

                    try:
                        port = int(input("PORT: "))
                    except KeyboardInterrupt:
                        print("\nProgram interrupted by user")
                        sys.exit()
                    except ValueError:
                        print(f"{Fore.RED}[!]{Fore.RESET} Error: Port is not a valid number")
                        time.sleep(2)
                        continue

                    if not is_port_available(host, port):
                        print(f"{Fore.RED}[!]{Fore.RESET} Error: The Port is occupied")
                        time.sleep(2)
                        continue

                    data["configuration"]["automatic"]["host"] = host
                    data["configuration"]["automatic"]["port"] = port
                    save_json()
                    continue















                if setting==option[1]:
                    sys.exit()
            elif put == option[4]:
                sys.exit()
            elif put not in option:
                print(f"{Fore.RED}[!]{Fore.RESET} Error: In user input")
                time.sleep(2)
                continue


            subprocess.run("cls", shell=True)
            data["configuration"]["lastSession"]["host"] = host
            data["configuration"]["lastSession"]["port"] = port
            save_json()
            break
            

except KeyboardInterrupt:
    print("\rProgram interrupted by user")
    sys.exit(0)

if __name__ == "__main__":
    main(host="localhost", port="55555")