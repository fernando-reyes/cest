#! /usr/bin/python

import RPi.GPIO as GPIO
import socket,time,os

BUTTON_PIN=7

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def printTicket():
	with cd("../printer"):
		os.system("./print.py")
	with cd("../rele"):
		os.system("./rele_entrada.py")
	print "DONE"

while True:
	
	time.sleep(0.1)
	
	if GPIO.input(BUTTON_PIN) == False:
		print('Pressed')
		#sendCommand()
		printTicket()
	
		while GPIO.input(BUTTON_PIN) == False: 
			time.sleep(0.1)
	
		print('Released')
