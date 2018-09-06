#!/bin/bash
exit
#echo ds3231 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
while true ; do
	hwclock --utc -s
	if [ "$?" -eq 0 ]; then
		break
	fi
done