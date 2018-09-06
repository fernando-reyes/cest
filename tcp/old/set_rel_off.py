#! /usr/bin/python

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.settimeout(3)
clientsocket.connect(('192.168.2.101', 8000))
clientsocket.send("PIND:9=1");
