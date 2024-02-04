# Libraries
import socket
from serverHost import *
from colorama import Fore, Back
import json




def server(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            print(f"{Fore.GREEN}[*] Server running on:{Fore.RESET} {host}:{port}")
    except Exception as e:
        main(host, port)

def json_load():
    with open('date.json', 'r') as f:
        # Load JSON data from the file
        data = json.load(f)

if __name__=="__main__":
    json_load()
    main(host="localhost", port="55555")
    session=data["configuration"]["session"]["id"]
    host=data["configuration"][session]["host"]
    port=data["configuration"][session]["port"]
    server(host,port)