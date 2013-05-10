#first try at multiprocessing
import sys
import timeit
import os
import multiprocessing
from collections import defaultdict
from TrueCasing import *
import time
import redis
import gzip
import mmap
class Project:
	def startAll(self):
		self.r = redis.Redis(port=6279,host='ip',db=0)
		self.rTime = 0

	def getTime(self):
		return self.rTime

	def __init__(self):
		self.startAll()
		self.map = makeDict(sys.argv[3])
		self.outputPath = sys.argv[2]
		self.input = sys.argv[1]
		self.count = 1

	def TrueCasing(self,l):
		#read the file f. ping redis. get output. multiply. get best. and write it 
		#print 'Name is ',multiprocessing.current_process().name		
		#print 'path to glory is ',self.outputPath
		#print 'path to future glory is ',self.input
		output = open(os.path.join(self.outputPath,'output'+str(l)),'w')
		f = open(self.input,'r')
		fil = mmap.mmap(f.fileno(),0,prot = mmap.PROT_READ)
		line = fil.readline()
		#print line
		while line:
			#print 'Sending redis time ', self.rTime
			sentence = truecase(self.r,line.split(' '),self.map)
			output.write(sentence+'\n') 
			#self.rTime += time
			#print 'After writing, redis time is ,', self.rTime			
			line = fil.readline()
		output.close()
		self.count+=1
		
		
if(len(sys.argv)<3):
	print 'python name.py input outputPath mapperFile numClients'
	sys.exit()


if __name__ == '__main__':
	startTime = time.time()
	project = Project()
	listNumbers = []
	jobs = []
	for i in range(0,int(sys.argv[4])):
		pawn = multiprocessing.Process(target = project.TrueCasing, args = (i,))
		jobs.append(pawn)
		listNumbers.append(i)
		pawn.start()
		#pawn.join()

	for j in jobs:
		j.join()
	#p.map(project.TrueCasing,listNumbers)
	#print project.count
	#while(project.count <= int(sys.argv[4])):	
	#	continue
	print sys.argv[4],'\t',time.time() - startTime	
	#print 'Total redis time is ', project.getTime()



#print numbers


