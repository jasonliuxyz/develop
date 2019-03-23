#logs.py
#22th 3 2019

"""
search for all *.log files in the given directory, zip them using the program you specitfy and ten date stamp them
"""

__author__ = 'Jason Liu'
__version__ = '1.0'

import os
import subprocess
from time import strftime


logsdir = '/tmp/liu'

for files in os.listdir(logsdir):
	if files.endswith(".log"):
		files1 = files + "." + strftime("%Y-%m-%d") + ".zip"
		os.chdir(logsdir)
		subprocess.call(['zip',files1,files])

		
