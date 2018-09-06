#!/usr/bin/python

from time import sleep
from module.nfc_522 import Nfc522
import os

nfc = Nfc522()

last1 = None
last2 = None

while True:
	
	id = nfc.reader1()
	if id <> last1: #validamos para no sobrecargar con escrituras...
		print "1=",id
		last1 = id
		if id:
			os.system("echo -n " + str(id) + " > lector_salida ")
		else:
			os.system("echo -n '' > lector_salida ")
	
	id = nfc.reader2()
	if id <> last2: #validamos para no sobrecargar con escrituras...
		print "2=",id
		last2 = id
		if id:
			os.system("echo -n " + str(id) + " > lector_entrada ")
		else:
			os.system("echo -n '' > lector_entrada ")
	
