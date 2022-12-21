import subprocess
import platform

interface = 'eth0'

if platform.system() == 'Windows':
    command = ['ipconfig']
else:
    command = ['ifconfig', interface]

result = subprocess.run(command, stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')

print(output)

import socket

hostname = socket.gethostname()

print("HostName of this device:",hostname)

ip_address = input("Enter the IP address to ping: ")

result = subprocess.run(['ping', '-n', '4', ip_address], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')

print(output)

import subprocess

ip_address = input("Enter the IP address to trace: ")

result = subprocess.run(['tracert', ip_address], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')

print(output)

import subprocess
import re

ip_address = input("Enter the IP address to get the VLAN for: ")

result = subprocess.run(['arp', '-a', ip_address], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')

# Use a regular expression to extract the interface name from the output
match = re.search(r"on (\S+)", output)
if match:
    interface = match.group(1)
    # Extract the VLAN number from the interface name
    vlan = int(interface.split(" ")[1])
    print(f"VLAN: {vlan}")
else:
    print("Unable to find VLAN in output")



print("THANK YOU FOR USING")