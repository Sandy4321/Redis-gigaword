'''
	Using a file, generate a file of key:value pairs . 
	key '\t' value 
	value will be the count of the word in the corpus
'''

import sys
import os
from collections import defaultdict
if(len(sys.argv)<2):
	print 'python name.py input output'
	sys.exit()

outputCounts = open(sys.argv[2],'w')
counts = defaultdict(int)
for line in open(sys.argv[1],'r'):
	words = line.split(' ')
	for w in words:
		counts[w]+=1

for word in counts:
	outputCounts.write(word+'\t'+str(counts[word])+'\n')

