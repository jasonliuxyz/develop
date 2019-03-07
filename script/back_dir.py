#!/usr/bin/python

import subprocess, time, os, sys

if len(sys.argv) < 2:
	print('python back.py source_dir target_dir')
	sys.exit(1)
else:
	source = sys.argv[1]
	target_dir = sys.argv[2]

#source = str(raw_input('need tar dir:'))
#target_dir = str(raw_input('tar target dir:'))

today_dir = target_dir + time.strftime('%Y%m%d')
time_file = time.strftime('%H-%M-%S') + '.zip'

target = today_dir + os.sep + time_file
zip_command = "zip -qr %s %s" %(target, ''.join(source))

if os.path.exists(today_dir) == 0:
	os.mkdir(today_dir)
if subprocess.call(zip_command, shell=True) == 0:
	print('success')
else:
	print('failed')
	
