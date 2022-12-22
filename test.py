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

# Prompt the user to enter a hostname or IP address
hostname = input("Enter the hostname or IP address for nslookup: ")

# Execute the nslookup command and capture the output
result = subprocess.run(['nslookup', hostname], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')

# Print the output
print(output)





