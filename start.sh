#!/bin/bash 

ROOT=/root/cest

#bajamos todo por si acaso...
./stop.sh

###### fuente de poder para salida (5v) lcd, scanner
/usr/local/bin/gpio -g mode 21 out
/usr/local/bin/gpio -g write 21 0

###### relé para led de entrada
/usr/local/bin/gpio -g mode 26 out
/usr/local/bin/gpio -g write 26 0

#exit

cd $ROOT/lcd
./lcd.py > /dev/null &

cd $ROOT/button
./button.py > /dev/null &

cd $ROOT/scanner
./scanner.py > /dev/null &

cd $ROOT/tarjetas
./entrada.py > /dev/null &
./salida.py > /dev/null &

#cd $ROOT/trn
#./get_7999_fserver.py > /dev/null &

#cd $ROOT/rfid
#./rfid.py > /dev/null &
#./lector_salida.py > /dev/null &
#./lector_entrada.py > /dev/null &
