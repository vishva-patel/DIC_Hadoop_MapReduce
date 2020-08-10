#!/usr/bin/python3
from nltk.stem import PorterStemmer
import sys
import re

for temp in sys.stdin:
	temp = temp.strip()
	temp = temp.lower()
    list1 = list()
	
    wordList = PorterStemmer()
	l= ["science","sea","fire"]
	line = re.findall(r"[A-Za-z]+'?[a-z]*",temp)
	
    for i in range(len(line)):
		temp = wordList.stem(line[i])
		if temp in l:
			line[i]="$"
	
    for i in range (len(line)-2):
		s=""
		if line[i]=="$" or line[i+1]=="$" or line[i+2]=="$":
			s=line[i]+'_'+line[i+1]+'_'+line[i+2]
			list1.append(s)
	
    for ans in list1:
		print("%s\t%s" % (ans,1))
