#!/usr/bin/env python
from collections import Counter
import sys
import re
 
words = {} 

for line in sys.stdin:
	line = line.strip()
	trigram, count= line.split('\t',1)
	count = int(count)
	words[trigram] = words.get(trigram,0) + count

ans = Counter(words)
tops = ans.most_common(10)

for top in tops:
	print("%s\t%s"%(top[0],top[1]))
