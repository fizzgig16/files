import re 
import sys

in_file = open(sys.argv[1],'r')
out_file = open(sys.argv[1] + ".new",'w')
for line in in_file:
	if ":" in line:
		line = re.sub(r'([a-zA-Z]+):([a-zA-Z]+)\(\)', r'\2(\1)', line)
		line = re.sub(r'([a-zA-Z]+):([a-zA-Z]+)\((.+)\)', r'\2(\1,\3)', line)
		line = re.sub(r'([a-zA-Z]+):([a-zA-Z]+)\(\)', r'\2(\1)', line)
		line = re.sub(r'([a-zA-Z]+):([a-zA-Z]+)\((.+)\)', r'\2(\1,\3)', line)
		line = re.sub(r'([a-zA-Z]+):([a-zA-Z]+)\(\)', r'\2(\1)', line)
		line = re.sub(r'([a-zA-Z]+):([a-zA-Z]+)\((.+)\)', r'\2(\1,\3)', line)
	if "hptrigger" in line:
		line = re.sub(r':hptrigger',r':hpTrigger',line)
	if "_G[" in line:
		line = re.sub(r'_G\[GetName\((.*),true\)\]',r'\1:GetEnv()',line)
	if "timer(" in line:
		line = re.sub(r'timer\(([a-zA-Z]+),', r'\1:timer(', line)
		line = re.sub(r'([a-zA-Z]+:timer\([^,]+,.+)\)[ \t]*$', r'\1,true)', line)
	if "EVENT_SIGNAL" in line:
		line = re.sub(r',([^,]+),([^)]+)',r',\2,\1',line)
	out_file.write(line)
in_file.close()	
out_file.close()