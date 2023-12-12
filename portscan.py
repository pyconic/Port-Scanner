import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Timeout of 1 second
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}.")
        else:
            print(f"Port {port} is closed on {ip}.")
        sock.close()
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")

def main():
    target_ip = input("Enter the IP address to scan: ")
    for port in range(1, 1025): # Scanning the first 1024 port_scan
        scan_port(target_ip, port)

if __name__ == "__main__":
    main()
