#! /usr/bin/python

import socket
import sys

#print sys.argv[1]

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.settimeout(3)
clientsocket.connect(('127.0.0.1', 8005))
clientsocket.send("PRINT");
print clientsocket.recv(512)