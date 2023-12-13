# Simple Port Scanner

# Description
This project is a Python-based simple port scanner tool. It is designed to check the status of TCP ports (open or closed) on a given IP address. The tool scans the first 1024 standard ports, providing a straightforward and user-friendly way to perform basic network reconnaissance.

# Features
• `Easy-to-Use`: Simple command-line interface for initiating scans. <br>
• `Range Scanning`: Scans the first 1024 ports of an IP address (well-known ports). <br>
• `Timed Connection Attempts`: Utilizes a timeout feature to enhance scanning speed. <br> 
• `Clear Output`: Outputs the status of each port (open or closed) on the target IP address.

# How it Works
• `Create Socket Connection`: Establishes a socket connection using IPv4 and TCP. <br>
• `Port Scanning`: Iterates through the first 1024 ports of the specified IP address. <br>
• `Status Check`: Checks if a port is open or closed by attempting to connect to it. <br>
• `Timeout Handling`: Incorporates a one-second timeout for each connection attempt to speed up the scanning process. <br>
• `Error Handling`: Catches and prints any socket errors encountered during the scan.

# Usage
1. Run the script in a Python environment. <br>
2. Enter the target IP address when prompted. <br>
3. The script will then scan and display the status of each port on the given IP address.

# Dependencies
1. `Python 3.x` <br>
2. `socket library` (standard Python library, no additional installation required)

# Limitations
The scanner only checks `TCP ports`. <br>
It scans a fixed range of ports `(1-1024)`, which might not include all services. <br>
`The tool is basic and doesn't provide advanced scanning options like stealth scans.`

# Note
`This tool is intended for educational purposes and network diagnostics. Always ensure you have authorization to scan the network or IP address in question to avoid legal issues.` <br>
`Scanning networks without permission can be interpreted as a hostile act by network administrators.`
