#create_dir_if_not_there.py
#Created: 21th 3 2019

"""
Checks to see if a directory exists in the users home directory, if not then create it
"""

__author__  = 'Jason Liu'
__version__ = '1.0'

import os

MESSAGE = 'The directory already exists.'
TESTDIR = 'testdir'

try:
	home = os.path.expanduser("~")
	print(home)

	if not os.path.exists(os.path.join(home, TESTDIR)):
		os.makedirs(os.path.join(home, TESTDIR))
	else:
		print(MESSAGE)

except Exception as e:
	print(e)
