#!/bin/sh
exit
while : ; do
	hwclock --utc -w
	if [ "$?" -eq 0 ]; then
		break
	fi
done