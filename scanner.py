#!/bin/python3

import sys
import socket
from datetime import datetime

#define our target

if len(sys.argv) == 2: #sys.argv is similar $1
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4 
else:
	print("Invalid amount of argument")
	sys.exit()
#python3 scanner.py <ip address> = $1, <hostname> = sys.argv[1]	

#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time Started: " +str(datetime.now()))
print("-" * 50)	

try: 
	for port in range(1,5665):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #return an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
	
except KeyboardInterrupt:
	print("\nExiting Program:")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()				

