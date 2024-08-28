import os
import platform
import sys

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def ping_host(host):
    # Determine the command based on the OS
    command = ['ping', '-n' if platform.system().lower() == 'windows' else '-c', '1', host.strip()]

    # Suppress the ping command output
    response = os.system(' '.join(command) + " > /dev/null 2>&1")

    # Determine if the host is reachable or not
    if response == 0:
        return f"{GREEN}reachable{RESET}"
    else:
        return f"{RED}not reachable{RESET}"

def main(filename):
    try:
        with open(filename, 'r') as file:
            hosts = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    
    # Ping each host and print the result
    for host in hosts:
        status = ping_host(host)
        print(f"Hosts: {host.strip()}\nPing: {status}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping.py host.txt")
        sys.exit(1)
    
    # Get the filename from the command line argument
    filename = sys.argv[1]
    
    main(filename)
