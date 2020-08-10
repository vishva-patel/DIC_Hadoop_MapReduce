#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd 

list1=[]
data = pd.read_csv("Test.csv")
test = data.values

for line in sys.stdin:
	temp = line.strip()
	temp = temp.split(',')
	label = temp[-1]
	train = temp[0:-1]
	nptrain = np.asarray(train,dtype=np.float64)
	test_1 = test.shape[0]

	for i in range(test_1):
		row = test[i]
		dist = np.linalg.norm(row-nptrain)
		print("%s&&%s&&%s"%(i,dist,label))





	
 
