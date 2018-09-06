#!/bin/sh

#echo ds3231 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
while : ; do
	hwclock --utc -r
	if [ "$?" -eq 0 ]; then
		break
	fi
done