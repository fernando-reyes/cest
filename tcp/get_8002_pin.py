#!/usr/bin/python

import os,string
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import listdir
from os.path import isfile, join

PORT_NUMBER = 8002

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		try:
			sendOk=False
			if self.path.startswith("/OPE/"):
				sendOk=True
				with cd("../rele"):
					if self.path[-3:] == "SAL":
						os.system("./rele_salida.py&")
					else:
						os.system("./rele_entrada.py&")

			if self.path.startswith("/PIN/"):
				sendOk=True
				os.system("../rele/set_pin.py "+string.replace(self.path[5:],","," "))

			if sendOk:
				self.send_response(200)
				self.end_headers()
				self.wfile.write( "OK" )
		except:
			self.send_error(405,'ERROR')

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('0.0.0.0', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()