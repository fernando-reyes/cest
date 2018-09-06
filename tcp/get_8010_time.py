#! /usr/bin/python

import socket,os
import datetime

print "Staring service..."  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 8010))  
sock.listen(5)
print "Started."

while True:  
	connection,address = sock.accept()  
	buf = connection.recv(1024)
	if( buf == "TIME" ):
		connection.send( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
	connection.close()
