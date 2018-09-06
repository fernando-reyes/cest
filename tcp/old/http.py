#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
from urlparse import urlparse

PORT_NUMBER = 8000

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
	try:

	    query = urlparse(self.path).query
	    query_components = dict(qc.split("=") for qc in query.split("&"))
	    cbar = query_components["cbar"]
	    print "CBAR=",cbar
	    self.send_response(200)
	    self.send_header('Content-type','text/html')
	    self.end_headers()
	    self.wfile.write("OK\n")

	except IOError:
	    self.send_error(404,'File Not Found: %s' % self.path)

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()