import socket  # Import the socket library for network connections

def scan_port(ip, port):
    try:
        # Create a new socket using IPv4 and TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout of 1 second for the socket

        # Attempt to connect to the specified IP and port
        result = sock.connect_ex((ip, port))

        # If the result is 0, the port is open
        if result == 0:
            print(f"Port {port} is open on {ip}.")
        else:
            # Otherwise, the port is not open (could be closed or filtered)
            print(f"Port {port} is closed on {ip}.")

        sock.close()  # Close the socket connection to free up resources
    except socket.error as err:
        # If a socket error occurs, print the error message
        print(f"Error scanning port {port}: {err}")

def main():
    # Prompt the user to enter an IP address for scanning
    target_ip = input("Enter the IP address to scan: ")

    # Iterate through ports 1 to 1024
    for port in range(1, 1025):
        scan_port(target_ip, port)  # Scan each port on the target IP

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
