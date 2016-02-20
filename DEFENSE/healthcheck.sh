#!/bin/bash

clear

echo "The script starts now"
touch file2
touch file3
i2cdetect -y -r 0 > file2
i2cdetect -y -r 1 >> file2
#echo "gibberish" >> file2 just to know that when it is different it works
diff -u results.txt file2 > file3

if [ -s file3 ]
then
   cat file3
   echo "file exists and not empty then something is wrong do not boot"
else
   echo "File exists but empty everything is safe"
fi

