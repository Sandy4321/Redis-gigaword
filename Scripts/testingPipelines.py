#for various numbers in input file, insert into redis and see how much time it takes
#assumes file is of the form  key '\t' value.  and is gzip
import sys
import os
import redis
from collections import defaultdict
if(len(sys.argv)<2):
	print 'python name.py input pipelinesizes'
	sys.exit()

r = redis.Redis(port=6379,host='localhost',db=0)
pipe = r.pipeline()
times = defaultdict(float)
for pipesize in open(sys.argv[2],'r'):
	count = 0
	pipesize = int(pipesize)
	startTime = time.time()
	for line in gzip.open(sys.argv[1],'rb'):
		parts = line.split('\t')
		key = parts[0]
		value = parts[1].rstrip('\n')
		if(count < pipesize):
			count += 1
			pipe.set(key,value)
		else:
			count = 0
			pipe.set(key,value)
			pipe.execute()
	times[pipesize] = (time.time() - startTime)
print times
