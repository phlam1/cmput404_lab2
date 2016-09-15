#!/usr/bin/env python

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#80 is the port server helps you identitfy type such as email http
clientSocket.connect(("www.google.ca", 80))

clientSocket.sendall("GET / HTTP/1.0\r\n\r\n")

while True:
	part = clientSocket.recv(1024)
	if (len(part) > 0):
		print part
	else: #part will be "" when the connection is done
		exit(0)
