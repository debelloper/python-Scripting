import socket
import threading

target = input("Enter target IP: ")
ports = range(1, 1025)

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    if s.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} open")

    s.close()

for port in ports:
    thread = threading.Thread(target=scan, args=(port,))
    thread.start()

if __name__ == "__main__":
    print(f"Scanning {target} for open ports...")