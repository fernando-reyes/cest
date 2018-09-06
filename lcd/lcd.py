#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_i2c.py
#  LCD test script using I2C backpack.
#  Supports 16x2 and 20x4 screens.
#
# Author : Matt Hawkins
# Date   : 20/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
# Copyright 2015 Matt Hawkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------
import smbus
import time
import RPi.GPIO as GPIO
import sys
import os.path

# Define some device parameters

#I2C_ADDR  = 0x26 # I2C device address
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 20   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3, 4)
#GPIO.setup(5, GPIO.ALT0,pull_up_down=GPIO.PUD_UP)

def lcd_init(I2C_ADDR_):
	# Initialise display
	lcd_byte(I2C_ADDR_,0x33,LCD_CMD) # 110011 Initialise
	lcd_byte(I2C_ADDR_,0x32,LCD_CMD) # 110010 Initialise
	lcd_byte(I2C_ADDR_,0x06,LCD_CMD) # 000110 Cursor move direction
	lcd_byte(I2C_ADDR_,0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
	lcd_byte(I2C_ADDR_,0x28,LCD_CMD) # 101000 Data length, number of lines, font size
	lcd_byte(I2C_ADDR_,0x01,LCD_CMD) # 000001 Clear display
	time.sleep(E_DELAY)

def bus_write_byte(I2C_ADDR_, bits):
	bus.write_byte(I2C_ADDR_, bits)

def lcd_byte(I2C_ADDR_,bits, mode):
	# Send byte to data pins
	# bits = the data
	# mode = 1 for data
	#        0 for command

	bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
	bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

	# High bits
	bus_write_byte(I2C_ADDR_, bits_high)
	lcd_toggle_enable(I2C_ADDR_,bits_high)

	# Low bits
	bus_write_byte(I2C_ADDR_, bits_low)
	lcd_toggle_enable(I2C_ADDR_,bits_low)


def lcd_toggle_enable(I2C_ADDR_,bits):
	# Toggle enable
	time.sleep(E_DELAY)
	bus_write_byte(I2C_ADDR_, (bits | ENABLE))
	time.sleep(E_PULSE)
	bus_write_byte(I2C_ADDR_,(bits & ~ENABLE))
	time.sleep(E_DELAY)

def lcd_string(I2C_ADDR_,message,line):
  # Send string to display
	message = message.ljust(LCD_WIDTH," ")
	lcd_byte(I2C_ADDR_, line, LCD_CMD)
	for i in range(LCD_WIDTH):
		lcd_byte(I2C_ADDR_,ord(message[i]),LCD_CHR)

def printMessage(I2C_ADDR_,line1,line2):
	tries = 10
	while tries:
		try:
			print "Trying ",line1,line2
			lcd_init(I2C_ADDR_)
			lcd_string(I2C_ADDR_,line1,LCD_LINE_1)
			lcd_string(I2C_ADDR_,line2,LCD_LINE_2)
			print "LCD:",line1,"/",line2
			break
		except:
			tries-=1
			#print "retrying..."
			#try:
			#  lcd_byte(I2C_ADDR,0x01, LCD_CMD)
			#except:
			#  pass 

fname = "./message"
line1 = "INSERTE TICKET"
line2 = "O PRESENTE TARJETA"

if __name__ == '__main__':
	printMessage(I2C_ADDR,line1,line2)
	while True:
		try:
			time.sleep(.1)
			if os.path.isfile(fname):
				time.sleep(.1)	#esperamos otro poco para que se alcance a grabar
				with open(fname) as f:
					content = f.readlines()
					os.remove(fname)
					if len( content ):
						content = (content[0]+";").split(";")
						if content[0] == '@':
							printMessage(I2C_ADDR,line1,line2)
						else:
							printMessage(I2C_ADDR,content[0], content[1])
		except KeyboardInterrupt:
			print "Cancel:", sys.exc_info()[0]
			lcd_byte(I2C_ADDR,0x01, LCD_CMD)
			break
		except:
			print "ERROR:", sys.exc_info()[0]
			try:
				lcd_byte(I2C_ADDR,0x01, LCD_CMD)
			except:
				"""
				"""
