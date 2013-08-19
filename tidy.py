import re
import sys

in_file = open(str(sys.argv[1] + ".old"),'r')
out_file = open(str(sys.argv[1] + ".lua"),'a')
tabs = 0
for line in in_file:
	line = line.lstrip()
	if re.search(r'^end',line.lstrip()):
		tabs = tabs - 1
	if re.search(r'^until',line.lstrip()):
		tabs = tabs - 1
	if re.search(r'^else',line.lstrip()):
		tabs = tabs - 1
	if tabs < 0:
		tabs = 0
	out_file.write("\t" * tabs + line.lstrip())
	if re.search(r'^if',line) or re.search(r'^for',line) or re.search(r'^function',line) or re.search(r'^repeat',line) or re.search(r'^while',line) or re.search(r'^else',line):
		if "end" not in line:
			tabs = tabs + 1

in_file.close()
out_file.close