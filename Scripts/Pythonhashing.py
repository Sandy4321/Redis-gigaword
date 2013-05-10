#use python hash method to distribute gigaword among 3 instances
import sys
import os
import gzip
import redis
from collections import defaultdict
PORT = 6179

r1 = redis.Redis(port=PORT,db=0,host='ip') #n1
r2 = redis.Redis(port=PORT,db=0,host='ip') #n2
r3 = redis.Redis(port=PORT,db=0,host='ip') #n3
pipe_r1 = r1.pipeline()
pipe_r2 = r2.pipeline()
pipe_r3 = r3.pipeline()

MAX = 10000
count_r1 = 0
count_r2 = 0
count_r3 = 0
ddict = defaultdict(int)
'''for line in gzip.open(sys.argv[1],'r'):
	if(len(line.split('\t')) < 2):
		continue
	parts = line.split('\t')
	key = parts[1].rstrip('\n')
	value = parts[0]
	m = hash(key) % 3
	ddict[m]+=1
print ddict
'''
for line in gzip.open(sys.argv[1],'r'):
	if(len(line.split('\t')) < 2):
		continue
	parts = line.split('\t')
	key = parts[1].rstrip('\n')
	value = parts[0]
	m =  hash(key) % 3
	if(m==0):
		if(count_r1 > MAX):
			pipe_r1.set(key,value)
			pipe_r1.execute()
			count_r1 = 0
		else:
			count_r1 += 1
			pipe_r1.set(key,value)
	elif(m==1):
		if(count_r2 > MAX):
			pipe_r2.set(key,value)
			pipe_r2.execute()
			count_r2 = 0
		else:
			count_r2 += 1
			pipe_r2.set(key,value)
	else:
		if(count_r3 > MAX):
			pipe_r3.set(key,value)
			pipe_r3.execute()
			count_r3 = 0
		else:
			count_r3 += 1
			pipe_r3.set(key,value)

		

