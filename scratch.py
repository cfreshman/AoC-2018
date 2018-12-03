import math
import re
import hashlib
import json
import copy

line = None
def read_line():
	global line
	try:
		line = input()
	except:
		line = None
	return line

lines = []
while read_line() != None:
	lines.append(line)

