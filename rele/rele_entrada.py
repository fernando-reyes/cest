#!/usr/bin/python

import os,string,time
import RPi.GPIO as GPIO
import common
common.run_once()

SENSOR_IN=12
PIN=11
ONE=0
TWO=1
P1=.1
P2=2
#TIM=1.5

#os.system("./set_pin.py %s %s %s %s" % (PIN,ONE,TWO,TIM))

#primer pulso
os.system("./set_pin.py %s %s %s %s" % (PIN,ONE,TWO,P1))

#segundo pulso, lo dejamos activado
os.system("./set_pin.py %s %s %s %s" % (PIN,TWO,ONE,P2))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR_IN, GPIO.IN,pull_up_down=GPIO.PUD_UP)

maxtimeout = 10
while (GPIO.input(SENSOR_IN) == False):
	#while True:
	time.sleep(1)
	maxtimeout-=1
	print "waiting...", maxtimeout 
	if maxtimeout < 0 :
		print "break" 
		break		

#esperamos antes de desactivar
time.sleep(2)

#y desactivamos
os.system("./set_pin.py %s %s %s %s" % (PIN,ONE,TWO,0))

#damos tiempo para que se baje la barrera
time.sleep(3)

