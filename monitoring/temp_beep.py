#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import sleep

while True:
	os.system("sensors | grep Package > temp.txt")
	file = open("temp.txt", "rw")
	content = file.read()
	file.close()
	content_arr = content.split("+")
	temp_arr = content_arr[1].split(".")
	temp = int(temp_arr[0])
	if temp > 90:
		os.system("beep -f 1000 -l 1500 -r 5")
	sleep(5)
