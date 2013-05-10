#average query answer time for one instance
from __future__ import division
import sys
import os
import redis
from TrueCasing import *
r = redis.Redis(port=6279,host='ip',db=0)
mapper = makeDict(sys.argv[2])
totalTime = 0
numQueries = 0
f = open(sys.argv[1],'r')
for line in f:
	words = line.split(' ')
	for w in words:
		options = mapper[w.lower()]
		for opt in options:
			startTime = time.time()
			value = r.get(opt)
			if(value is None):
				value = -100
			numQueries +=1
			totalTime += (time.time() - startTime)
print totalTime,'\t',numQueries,'\t',totalTime/numQueries
f.close()
f = open(sys.argv[1],'r')
dtime = 0
dQueries = 0
timeHashing = 0
pythonHashing = 0
n1 = redis.Redis(port=6379,host='ip',db=0)
n2 = redis.Redis(port=6379,host='ip',db=0)
n3 = redis.Redis(port=6379,host='ip',db=0)
bucket = 0
for line in f:
	words = line.split(' ')
	for w in words:
		options = mapper[w.lower()]
		for opt in options:
			dQueries += 1
			hashStart = time.time()
			h = hashing(opt)
			timeHashing += time.time() - hashStart
			startpH = time.time()

			ph = hash(opt)
			bucket = ph % 3
			pythonHashing += time.time() - startpH

			if(h==0):
				start = time.time()
				v = n1.get(opt)
				if(v is None):
					v = -100
				dtime += (time.time() - start)
			elif(h==1):
				start = time.time()
				v = n2.get(opt)
				if(v is None):
					v = -100
				dtime += (time.time() - start)
			else:
				start = time.time()
				v = n3.get(opt)
				if(v is None):
					v = -100
				dtime += (time.time() - start)
			
print dtime,'\t',dQueries,'\t',dtime/dQueries
print 'hash time  is ',timeHashing
print 'hash time python is ',pythonHashing
f.close()

				

