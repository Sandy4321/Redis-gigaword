'''
	Writes a set of key:value pairs into a redis instance . change port and host according to need
	the maximum is 10,000. use Scripts/TestingPipelines to decide your magic number. 
	Execution : python writingGiga.py <filename>
'''

import gzip
import sys
import os
import redis
import time
if(len(sys.argv)<2):
	print 'python name.py inputfile'
	sys.exit()

startTime = time.time() 
r = redis.Redis(port=6279,host='localhost',db=0)
pipe = r.pipeline(transaction=True)
i = 0
MAX = 10000
for line in gzip.open(sys.argv[1],'rb'):
	if('\\' not in line and '=' not in line):
		try:	
			parts = line.split('\t')
		
		
			key = parts[1].rstrip('\n')
			value = parts[0]
			if(i<MAX):
				i=i+1
				pipe.set(key,value)
			else:
				i=0
				pipe.set(key,value)
				pipe.execute()
				i=i+1
		except:
			print line
print time.time() - startTime, 'seconds '
