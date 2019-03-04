#!/usr/bin/python

import os, sys
import ConfigParser

class Config:
	def __init__(self, path):
		self.path = path
		self.cf = ConfigParser.ConfigParser()
		self.cf.read(self.path)

	def get(self, field, key):
		result = ""
		try:
			result = self.cf.get(field, key)
		except:
			result = ""
		return result	
		
	def set(self, field, key, value):
		try:
			self.cf.set(field, key, value)
			self.cf.write(open(self.path, "w"))
		except:
			return False
		return True

if __name__ == "__main__":
	a = Config("/data/developfirst/script/toolhire.ini")
	result = a.get("baseconf", "host")
	print(result)
