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
		with open("lector_salida") as f:
			content = f.readlines()
		if len( content ):
			id = content[0]
	finally:
		return id

mastercard = "307664880423"
while True:
	sleep( .1 )
	id = getId()
	if id:
		id = str( id )
		if id == mastercard:
			while True:
				os.system("echo -n 'ACERQUE TARJETA;A AGREGAR/ELIMINAR' > ../lcd/message")
				while ( getId() <> None ): #esperamos a que aleje la tarjeta maestra
					sleep( .1 )
				id = None
				before = datetime.today()
				while ( ( datetime.today() - before ).seconds < 10 ) and ( id == None ):
					id = getId()
					sleep( .1 )
				while( getId() <> None ): #esperamos a que aleje la tarjeta
					sleep( .1 )
				if ( id == None ) or ( str( id ) == mastercard ):
					break
				id = str( id )
				if os.path.isfile( "../data/authcards/" + id ):
					os.system( "rm -rf ../data/authcards/" + id )
					os.system("echo -n 'TARJETA ELIMINADA;CON EXITO' > ../lcd/message")
				else:
					os.system( "touch ../data/authcards/" + id )
					os.system("echo -n 'TARJETA AGREGADA;CON EXITO' > ../lcd/message")
				sleep(2)
			os.system("echo -n '@' > ../lcd/message")
		elif os.path.isfile( "../data/authcards/" + id ):	#auth
			os.system("echo '" + now() + "' > ../trn/salidas/tarjetas/"+id ) 
			with cd("../rele"):
				os.system("./rele_salida.py")
		else:
			os.system("echo -n 'TARJETA NO;REGISTRADA' > ../lcd/message")
			sleep(4)
			os.system("echo -n '@' > ../lcd/message")
