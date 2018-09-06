#! /usr/bin/python

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.settimeout(3)
clientsocket.connect(('192.168.2.12', 8000))
clientsocket.send("REL1:ON\n");
