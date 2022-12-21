# Network-Police
Basic network troubleshooting script
This Python program performs several tasks related to networking:

It uses the subprocess module to run the ifconfig or ipconfig command (depending on the operating system) to get information about the network interfaces on the computer.

It gets the hostname of the computer using the socket module.

It prompts the user to enter an IP address and uses the subprocess module to run the ping command to send ICMP echo request packets to the specified IP address.

It prompts the user to enter an IP address and uses the subprocess module to run the tracert command to trace the route to the specified IP address.

It prompts the user to enter an IP address and uses the subprocess module to run the arp command to display the ARP cache for the specified IP address. It then uses a regular expression to extract the interface name from the output, and parses the VLAN number from the interface name.

