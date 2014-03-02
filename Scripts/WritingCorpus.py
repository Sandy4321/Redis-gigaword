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
r = redis.Redis(port = 6279, host = 'localhost', db = 0)
pipe = r.pipeline(transaction = True)
i = 0
MAX = 10000
with os.popen('zcat ' + sys.argv[1]) as arpa_file:
	#this is done because gzip files are slowly read when using gzip.open(). this one is fastest, relatively
	for line in arpa_file:
		if('\\' not in line and '=' not in line):#this is only when using the ARPA file. 
			try:	
				parts = line.split('\t')
				key = parts[1].rstrip('\n')
				value = parts[0]
				pipe.set(key, value)
				if(i<MAX):
					i=i+1
				else:
					i=0
					pipe.execute()
					i=i+1
			except:
				print line
print time.time() - startTime, 'seconds '
