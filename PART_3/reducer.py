#!/usr/bin/python3
import sys
import re
output_data = {}

# Iterate the output produced from mapper.py
for line in sys.stdin:
	line = line.strip()
	output_key, file_name = re.split('\t',line)
	if output_key in output_data:
		if file_name in output_data[output_key]:
			continue
		# Case 1 - add file_name to the result
		else:
			output_data[output_key].append(file_name)
	# Case 2 - add output_key and file_name to the result
	else:
		output_data[output_key] = []
		output_data[output_key].append(file_name)

# Produce reducer output
for output_key in output_data:
	print("%s\t%s"%(output_key, output_data[output_key]))

              


