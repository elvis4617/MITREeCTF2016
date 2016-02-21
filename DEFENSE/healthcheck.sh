#!/bin/bash

clear

touch file2
touch file3

#Add data of i2c mapping to file2 for busses 0 and 1, ignoring 2
i2cdetect -y -r 0 > file2
i2cdetect -y -r 1 >> file2

#Attempt at enabling and transferring map for bus 2
#if [ ! -f /sys/devices/bone_capemgr.9/slots 
#	echo "[8BWh!t3]" | sudo -S [ echo BB-I2C1 > /sys/devices/bone_capemgr.9/slots ]
#fi
#i2cdetect -y -r 2 >> file2

#A test to make sure the program works on positive diff
#echo "gibberish" >> file2

#Add data of what is different between what is expected and what is found to file 3
diff -u results.txt file2 > file3

#If there is a difference between what is expected and what is found, reboot
if [ -s file3 ]
then
   cat file3
   printf "\nSystem has different setup, do not boot\n\n"
	echo "[8BWh!t3]" | sudo -S reboot
else
   printf "\nEverything is safe :)\n\n"
fi
