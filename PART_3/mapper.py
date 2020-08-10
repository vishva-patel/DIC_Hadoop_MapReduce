#!/usr/bin/python3
import re
import os
import sys
import nltk
from nltk.corpus import stopwords

stop_words = list(set(stopwords.words('english')))

# Iterate for each record for all files in the given directory
for line in sys.stdin:
	line = line.strip().split() 
	for counter in range(0, len(line)):
		# Get the file name
		full_file_name = os.environ['map_input_file']
		split_file_name = full_file_name.split('/')
		file_name = split_file_name[len(split_file_name) - 1]

		# Update the word
		word = line[counter].lower()
		word = re.findall(r"[a-z]+'?[a-z]*",word)

		# Produce the mapper output
		# if (len(word) != 0 and word not in stop_words):
		if word not in stop_words:
			if len(word) != 0:
				print("%s\t%s" % (word, file_name))