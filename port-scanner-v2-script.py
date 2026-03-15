import socket
import threading

target = input("Enter target IP: ")
ports = range(1, 1025)

def scan(port): # Function to scan a single port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
    socket.setdefaulttimeout(1)

    if s.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} open")

    s.close()

for port in ports: # Loop through the specified range of ports
    thread = threading.Thread(target=scan, args=(port,)) # Create a new thread for each port scan
    thread.start()

if __name__ == "__main__":
    print(f"Scanning {target} for open ports...")