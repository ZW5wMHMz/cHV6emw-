#!/usr/bin/env python

import psutil
import os
from time import sleep

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

while True:
	if plugged and percent > 78:
		for i in range(5):
			os.system("beep -f 1000 -l 100 -r 2 -d 100")
			sleep(0.5)
	sleep(5)
