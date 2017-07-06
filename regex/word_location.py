#!/bin/python3

import re

file = open('sample.txt', 'r')
line_num = 1

for line in file:
	for match in re.finditer(r'\bDogFood\b', line):
		print ("Found", match.group(0), "in line", line_num, 
				"at indexes", match.start(), "-", match.end())
	line_num += 1

file.close()



