#burpsuite
import socket
import datetime

target = input("Enter target IP address: ")

def port_scanner(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Scanning the target {ip}...")
        print("Time started: ",datetime.now())

        for port in range(20,90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()

port_scanner(target)