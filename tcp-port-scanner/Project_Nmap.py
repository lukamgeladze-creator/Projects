import sys
import argparse
import socket
import threading
from datetime import datetime as dt 
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

#Function to scan a port

def scan_port(target,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator -> if 0 port is open if 1 port is closed
        s.close()

        if result == 0:
            return port, "open"
        elif result == socket.errno.ECONNREFUSED:
            return port, "closed"
        else:
            return port, "filtered"
    except socket.error:
        return port, "filtered"

#main function -> argument validation and target definition

results_lock = Lock()

def thread_worker(target, port, results):
    result = scan_port(target, port)
    with results_lock:  # Lock before appending
        results.append(result)

def parse_ports(port_arg):  
    if ',' in port_arg:
        return [int(p) for p in port_arg.split(',')]
    elif '-' in port_arg:
        start, end = port_arg.split('-')
        return list(range(int(start), int(end) + 1))
    else:
        return [int(port_arg)]

def main():
    
    parser = argparse.ArgumentParser(description='TCP Port Scanner')
    parser.add_argument('target', help='Target IP or hostname')
    parser.add_argument('-p', '--ports', default='1-1000', help='Port range (default: 1-1000)')
    parser.add_argument('-t', '--threads', type=int, default=100, help='Number of threads (default: 100)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show closed/filtered ports')
    args = parser.parse_args()

    target = args.target 

    # Parse port range
    results = []

    #resolve target ip
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"unable to resolve hostname: {target}")
        sys.exit(1)
    
    #Add a pretty banner
    print("-" * 50)
    print(f"scanning target: {target_ip}")
    print(f"scanning started at: {dt.now()}")
    print("-" * 50)

    port_range = parse_ports(args.ports)

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(lambda port: thread_worker(target_ip, port, results), port_range)

    for port, state in sorted(results):
        if state == "open":
            print(f"[+] Port {port} is open")
        elif args.verbose:
            print(f"[-] Port {port} is {state}")

    print("\nScanning completed.")

if __name__ == "__main__":
    main()
else:
    print("This script is intended to be run as a standalone program.")

