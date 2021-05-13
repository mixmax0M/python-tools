# %%
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Input the IP Adress for port scanning: ")
port = int(input("\nType in the port you would like to scan: "))

def portScan(port):
    if s.connect_ex((host, port)):
        print(f"The port {port} is closed.")
    else:
        print(f"The Port {port} is open.")
portScan(port)