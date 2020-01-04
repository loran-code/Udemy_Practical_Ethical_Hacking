#!/bin/python

import sys
import socket
from datetime import datetime

#Define your target (IP)
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add a banner for easy readable information
print("-" * 50)
print("Scanning target " + target)
print(" Time started: " + str(datetime.now()))
print("-" * 50) 

try: 
	for port in range(1,100): #1 till 65535 for all ports
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket = IPv4 - Sock = port
		socket.setdefaulttimeout(0.1)
		result = s.connect_ex((target,port)) #returns an error indicator
		print("Checking port {}".format(port))		
		if result == 0:
			print("Port {} is open".format(port))
		s.close()


except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print ("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print ("Couldn't connect to sserver.")
	sys.exit()
