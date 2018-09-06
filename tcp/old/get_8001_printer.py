#! /usr/bin/python

import socket,os

print "Staring service..."  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 8001))  
sock.listen(5)
print "Started."

while True:  
	connection,address = sock.accept()  
	buf = connection.recv(1024)
#	print buf
	if( buf == "PRINT" ):
		print "imprime"
		os.system("../printer/print.py")
		connection.send("OK")
	connection.close()
