import socket
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor

# List of ANSI color codes
def purple(text: str) -> str:
    # Wrap text in ANSI codes for purple color
    return f"\033[35m{text}\033[0m"

def blue(text: str) -> str:
    # Wrap text in ANSI codes for blue color
    return f"\033[34m{text}\033[0m"

def red(text: str) -> str:
    # Wrap text in ANSI codes for red color
    return f"\033[31m{text}\033[0m"

def bold(text: str) -> str:
    # Wrap text in ANSI codes for bold
    return f"\033[1m{text}\033[0m"

equalSign = "="
emptySpace = " "

def eye_art():
    art = [
        "     ________ ",
        "    /  /  \\  \\   ",
        "   |  /    \\  | ",
        "   |  | 🧿 |  | ",
        "   |  \    /  | ",
        "    \__\__/__/  "
    ]
    
    for line in art:
        print(blue(line))
    print()

def trademark(main):
    eye_art()
    def wrapper():
        print(purple(bold((emptySpace * 2) + "The Raven's Eye")))
        print(purple(equalSign * 19))
        print(red("By: RavenTheBird789"))
        print(purple(equalSign * 19))
        print(purple("Please select an option:"))
        print(purple("1. Resolve A Hostname"))
        print(purple("2. Port Scan Of A Given Hostname"))
        print(purple("3. Exit"))
        main()
    return wrapper

def user_request():
    prompt = input(("\nWould you like to use the tool again? (yes/no): "))
    if prompt == "yes":
        os.system('clear')
        eye_art()
        main()
    elif prompt == "no":
        os.system('clear');
        text = "Blessed Is The Sacred Raven's Eye, And Blessed Are Those Who Know How To Wield Its Power."
        for char in text:
            sys.stdout.write(purple(char))
            sys.stdout.flush()
            time.sleep(0.05)
        os.system('clear');
        os._exit(0);
    else:
        os.system('clear')
        print(red("Invalid input"))
        time.sleep(3)
        os.system('clear')
        user_request()

def resolve(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return f"[+] IP Address Resolved For Hostname: {ip}"
    except socket.gaierror as e:
        return f"[-] Couldn't resolve {hostname}: {e}"

def scan_port(target_host, port):
    """Attempts to connect to a specific TCP port. Returns the port number if open, otherwise None."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        # connect_ex returns 0 if the connection succeeded, or an error code if it failed
        result = s.connect_ex((target_host, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            return port
    return None
    
def port_scan():
    target_host = input("Enter the target hostname: ")
    start_port = int(input("Start port: ") or 1)
    end_port = int(input("End Port: ") or 1024)
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[-] Hostname '{target_host}' could not be resolved.")
        sys.exit()

    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Scanning Ports : {start_port} to {end_port}")
    print("-" * 50)

    open_ports = []
    ports_to_scan = range(start_port, end_port + 1)
    
    # You can adjust max_workers to change speed (higher = faster, but heavier on network)
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(target_ip, p), ports_to_scan)
        open_ports = [port for port in results if port is not None]

    print("-" * 50)
    print("Scan complete.")
    print(f"Open ports found: {open_ports}")
    
@trademark
def main():
    choice = input(purple("Enter your choice (1-3): "))
    if choice == '1':
        hostname = input("Enter the hostname: ").strip()
        resolution = resolve(hostname)
        print(resolution)
        time.sleep(3)
        user_request()
    elif choice == '2':
        port_scan()
        time.sleep(3)
        user_request()
    elif choice == '3':
        os.system('clear');
        text = "Blessed Is The Sacred Raven's Eye, And Blessed Are Those Who Know How To Wield Its Power."
        for char in text:
            sys.stdout.write(purple(char))
            sys.stdout.flush()
            time.sleep(0.05)
        os.system('clear');
        os._exit(0);
    else:
        print(red(bold("Invalid choice. Please try again.")))
        time.sleep(3)
        os.system('clear')
        eye_art()
        main();
main();