#!/usr/bin/python

from time import sleep
from datetime import datetime
import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def now():
	return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def getId():
	id = None
	try:
		with open("lector_entrada") as f:
			content = f.readlines()
		if len( content ):
			id = content[0]
	finally:
		return id

last1 = None
while True:
	sleep( .1 )
	id = getId()
	if id:
		print id
		id = str( id )
		if os.path.isfile( "../data/authcards/" + id ):	#auth
			print id,",AUTH=OK"
			os.system("echo '" + now() + "' > ../trn/entradas/tarjetas/"+id ) 
			with cd("../rele"):
				os.system("./rele_entrada.py")
		else:
			print id,",AUTH=NO"
			sleep(2)
