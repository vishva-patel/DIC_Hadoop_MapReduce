#!/usr/bin/env python

import sys
import re
K=13
distance={}
predictions={}

for line in sys.stdin:
	line = line.strip()
	testno,dist,label= line.split('&&')
	testno=int(testno)
	label=int(label)
	dist=float(dist)
	try:
		distance[testno].append((dist,label))
	except:
		distance[testno]=[]
		distance[testno].append((dist,label))

for key, val in sorted(distance.items()):
	temp=sorted(val,key=lambda x:x[0])[:K]
	list1=[]
	for i in range(K):
		list1.append(temp[i][1])
	pred = max(set(list1),key=list1.count)
	print("%s\t%s"%(key,pred))


	
