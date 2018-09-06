#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: utf-8 -*-
ñáéíóú=\xa4\xa0\x82\xa1\xa2\xa3
ÑÁÉÍÓÚ=\xa5\xb5\x90\xd6\xe0\xe9
"""

from escpos.printer import Network
from escpos.printer import Serial
from escpos.printer import Usb
import datetime

now=datetime.datetime.now()
id = now.strftime("%d%m%H%M%S") #+"P"
open( '../trn/entradas/tickets/'+id , 'w').write( now.strftime("%Y/%m/%d %H:%M:%S") )


#p = Usb(  0x04b8, 0x0e15 )
p = Usb(  0x0525, 0xa700 )
#p = Network( host="192.168.2.102" )
#p = Serial( devfile = "/dev/ttyUSB0", baudrate=9600 )
#p = Serial( devfile = "/dev/ttyUSB0", baudrate=19200 )
#p = Serial( devfile = "/dev/ttyUSB0", baudrate=9600 )

#p._raw('\x1b\x74\x19') #charmap euro
#p._raw("ANFION MU\xa5OZ 380\n" )

#p._raw('\x1b\x74\x19') #charmap euro


#p._raw('\x1b\x61\x00')
p.barcode( code=id , bc='CODE39',height=150,width=2) #width=3,font="B" )
p.charcode('MULTILINGUAL')
#p._raw('\x1b\x74\x19')
p._raw("\n")
#p._raw('\x1b\x61\x30')
p.set( 'CENTER','A','normal',1 )
p._raw("ESTACIONAMIENTO\n")
p._raw("ANFION MU\xa5OZ 360\n" )
p._raw("\n")
p.set( 'LEFT' )
#p.charcode('MULTILINGUAL')
#p._raw('\xa4\xa0\x82\xa1\xa2\xa3')
p._raw("Hector Ramon Martinez Cartes\n")
p._raw("Rut: 6281483-8\n")
p._raw("\n")
p._raw("\n")
p._raw("Tarifa:\n")
p._raw("Cada minuto efectivo $25 pesos\n")
p._raw("Horario atenci\xa2n Invierno \n")
p._raw("Desde 07:00 a 23:00 hrs.\n")
p._raw("Horario atenci\xa2n resto del a\xa4o\n")
p._raw("Desde 07:00 a 00:00 hrs.\n")
p._raw("\n")
p._raw("CONSERVE EL TICKET\n")
p._raw("VALIDE TICKET AL SALIR\n")
p._raw("\n")
p.set( 'LEFT','A','B',1 )
p._raw("NO DEJAR OBJETOS DE VALOR EN\n")
p._raw("VEH\xd6CULO\n")
p._raw("PAGUE CASETA DE TAXIS\n")
p._raw("\n")
p._raw("ENTRADA\n")
p._raw("\n")
p.set( 'LEFT','A','normal',1 )
date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")
p._raw("FECHA y HORA:"+date+"\n")
p._raw("             "+time+"\n")
p._raw("\n")
p._raw("VALE CONTROL INTERNO\n")
p._raw("NO V\xb5LIDO COMO BOLETA DE VENTA\n")
p.cut()
#p._raw(b'\x1d'+b'V'+b'\x30' )	#corte FULL de papel
#with open( id , 'a') as the_file:
#    the_file.write( now.strftime("%d%m%H%M%S") )
