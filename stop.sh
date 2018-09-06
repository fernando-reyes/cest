#!/bin/bash 

killall lcd.py rfid.py lector_entrada.py lector_salida.py button.py scanner.py entrada.py salida.py 
#get_7999_fserver.py

###### fuente de poder (5v) comun para salida
/usr/local/bin/gpio -g write 21 1

##### relé para led de entrada
/usr/local/bin/gpio -g write 26 1
               
###### pin reset de lectores de tarjeta
#/usr/local/bin/gpio -g write 22 0
#/usr/local/bin/gpio -g write 27 0