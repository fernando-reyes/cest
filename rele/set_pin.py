#! /usr/bin/python

#3.3v
import sys
import RPi.GPIO as GPIO
from time import sleep

PIN=int(sys.argv[1])
ONE=int(sys.argv[2])
TWO=int(sys.argv[3])
TIM=float(sys.argv[4])

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT, initial=TWO)

GPIO.output(PIN, ONE)
sleep(TIM)
GPIO.output(PIN, TWO)
