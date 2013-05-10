#use hashes to write gigaword. use hashing to decide which bucket. use 82000 buckets in total 
import sys
import os
import gzip
import redis
def h(string):
	return hash(string)

r = redis.Redis(port=6479,host='localhost',db=0)
pipe = r.pipeline()
count = 0
MAX = 10000
for line in gzip.open(sys.argv[1],'rb'):
	if(len(line.split('\t')) < 2):
		continue
	parts = line.split('\t')
	key = parts[1].rstrip('\n')
	value = parts[0]
	bucket = h(key) % 82000
	if(count < MAX):
		count += 1
		pipe.hset(bucket,key,value)
	else:
		count = 0
		pipe.hset(bucket,key,value)
		pipe.execute()

