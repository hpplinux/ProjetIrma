#!/usr/bin/python3

import os
import colors as color
from sys import argv

# Author Alexis LE MASLE

if len(argv) < 3:
	print(color.LIGHT_BLUE_1 + "Use:")
	print("./ExecConfig.py [num .config] [nb core]" + color.GRAY)
	exit(0)

if int(argv[2]) <= 0:
	print(color.RED + "Please enter a non zero positive number of core." + color.GRAY)
	exit(0)

# It runs with a different behavior
cmd = "/TuxML/tuxml.py /TuxML/linux-4.13.3/ -d /TuxML/gcc-learn/" + argv[1] + ".config -c " + argv[2]
os.system(cmd)
