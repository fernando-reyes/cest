#!/usr/bin/python

import os
import datetime
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urlparse import parse_qs, urlparse
from os import listdir
from os.path import isfile, join

PORT_NUMBER = 7999

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

			if self.path.startswith("/GET/"):
				path=self.path[5:]
				self.send_response(200)
				self.end_headers()
				onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
				self.wfile.write(','.join(onlyfiles))

			if self.path.startswith("/DEL/"):
				os.remove( self.path[5:] )
				self.send_response(200)
				self.end_headers()
				self.wfile.write("OK")

			if self.path.startswith("/TIM/GET/"):
				self.send_response(200)
				self.end_headers()
				self.wfile.write( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )

			if self.path.startswith("/TIM/SET/"):
				params = parse_qs( urlparse(self.path).query )
				os.system("date --set '%s %s'" % (params["date"][0],params["time"][0]))
				self.send_response(200)
				self.end_headers()
				self.wfile.write("OK")

			if self.path.startswith("/PWR/"):
				self.send_response(200)
				self.end_headers()
				self.wfile.write("OK")
				if self.path[5:] == "REBOOT":
					os.system("reboot")

			if self.path.startswith("/SRV/"):
				self.send_response(200)
				self.end_headers()
				self.wfile.write("OK")
				if self.path[5:] == "DOWN":
					with cd(".."):
						os.system("./down.sh")
				if self.path[5:] == "UP":
					with cd(".."):
						os.system("./up.sh")

			if self.path.startswith("/OPE/"):
				self.send_response(200)
				self.end_headers()
				self.wfile.write("OK")
				if self.path[5:] == "ENT":
					with cd("../rele"):
						os.system("./rele_entrada.py&")
				if self.path[5:] == "SAL":
					with cd("../rele"):
						os.system("./rele_salida.py&")

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path[5:])
		except OSError:
			self.send_error(404,'File Not Found: %s' % self.path[5:])
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
