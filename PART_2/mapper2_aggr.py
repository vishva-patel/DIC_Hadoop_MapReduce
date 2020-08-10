#!/usr/bin/env python
import sys
import re

for temp in sys.stdin:
	temp = temp.strip()
	trigram, count= temp.split('\t',1)
    
	print("%s\t%s"%(trigram,count))