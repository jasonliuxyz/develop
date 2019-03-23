#get_pid.py
#Created: 21th 3 2019

"""
get the process id
"""

__author__ = "Jason liu"
__version__ = "1.0"

import subprocess
import logging

def getPid(process):
	cmd = "ps aux | grep '%s' | grep -v grep " % process
	logging.info(cmd)
	out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	infos = out.stdout.read().splitlines()
	pidlist = []
	if len(infos) >= 1:
		for i in infos:
			pid = i.split()[1]
			if pid not in pidlist:
				pidlist.append(pid)
		return pidlist
	else:
		return -1

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	gameproc = ["nginx"]
	for process in gameproc:
		pid = getPid(process)
		print(pid)
