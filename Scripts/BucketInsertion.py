#insert these into buckets
import sys
ip = sys.argv[1]
f = sys.argv[2]
import os
import redis 
r = redis.Redis(port=6379,db=0,host=ip)
pipe = r.pipeline(transaction=True)

MAX = 10000
iCount = 0
for line in open(f,'r'):
	parts = line.split('\t')
	key = parts[0].rstrip('\n')
	value = parts[1].rstrip('\n')
	if(iCount < MAX):
		iCount += 1
		pipe.set(key,value)
	else:
		pipe.set(key,value)
		pipe.execute()
		iCount = 0

