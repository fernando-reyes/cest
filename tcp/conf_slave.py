#! /usr/bin/python

import socket
import sys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.settimeout(3)
clientsocket.connect(('192.168.2.12', 8000))
clientsocket.send("SET_REMOTE:192.168.2.11");
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.settimeout(3)
clientsocket.connect(('192.168.2.12', 8000))
clientsocket.send("SET_CBAR:8001");
