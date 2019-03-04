#!/usr/bin/python

import os, json

def test_dumps():
	tmp_dict = {
		"apple": "red",
		"fish": "water",
		"cat": "black"
	}
	print(type(tmp_dict))
	tmp_dict = json.dumps(tmp_dict)
	print(type(tmp_dict))

def test_loads():
	tmp_dict = {
		"apple": "red",
		"fish": "water",
		"cat": "black"
	}
	tmp_dict = json.dumps(tmp_dict)
	print(type(tmp_dict))
	tmp_dict = json.loads(tmp_dict)
	print(type(tmp_dict)) 

def test_dump():
	tmp_dict = {
                "apple": "red",
                "fish": "water",
                "cat": "black"
        }
	file = 'one.json'
	with open(file, 'w') as f:
		json.dump(tmp_dict, f)

def test_load():
	tmp_dict = {}
	file = 'one.json'
	with open(file, 'rb') as f:
		date = json.load(f)
		print(date)

if __name__ == "__main__":
	test_dumps()
	test_loads()
	test_dump()
	test_load()
