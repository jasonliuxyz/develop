#move_files_over_x_days.py
#22th 3 2019

"""
This will move all the files from the src directory that are over 240days old to the destination directory
"""

import shutil
import sys
import time
import os
import argparse

usage = 'python move_files_over_x_days.py -src [SRC] -dst [DST] -days [DAYS]'
description = 'Move files from src to dst if they are older than a certain number of days.  Default is 240 days'

args_parser = argparse.ArgumentParser(usage=usage, description=description)
args_parser.add_argument('-src', '--src', type=str, nargs='?', default='.', help='(OPTIONAL) Directory where files will be moved from. Defaults to current directory')
args_parser.add_argument('-dst', '--dst', type=str, nargs='?', required=True, help='(REQUIRED) Directory where files will be moved to.')
args_parser.add_argument('-days', '--days', type=int, nargs='?', default=240, help='(OPTIONAL) Days value specifies the minimum age of files to be moved. Default is 240.')
args = args_parser.parse_args()

if args.days < 0:
	args.days = 0

src = args.src
dst = args.dst
days = args.days
now = time.time()

if not os.path.exists(dst):
	os.mkdir(dst)

for f in os.listdir(src):
	f = src + '/' + f
	if os.stat(f).st_mtime < now - days * 86400:
		if os.path.isfile(f):
			shutil.move(f, dst)
