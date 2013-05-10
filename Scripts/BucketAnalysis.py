#are all the servers getting the same number of queries ? 
import sys
import os

from TrueCasing import *
numN1 = 0
numN2 = 0
numN3 = 0
mapper = makeDict(sys.argv[2])
for line in open(sys.argv[1],'r'):
	words = line.split(' ')
	for opt in words:
		options = mapper[opt.lower()]
		for w in options:
			h = hash(w)
			if(h==0):
				numN1 +=1
			elif(h==1):
				numN2 +=1
			else:
				numN3 +=1
print numN1,'\t',numN2,'\t',numN3
