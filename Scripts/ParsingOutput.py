#we have the output . need to parse it to make a list 
import sys
import os
for f in os.listdir(sys.argv[1]):
	print f
	output = open('output_' + str(f),'w')
	for r in os.listdir(os.path.join(sys.argv[1],f)):
		data = open(os.path.join(sys.argv[1],f,r),'r')
		
		for line in data:
			parts = line.split('\t')
			output.write(parts[0]+' '+parts[1].rstrip('\n')+'\n')
 
	#output = open(os.path.join(sys.argv[1],'output-'+str(f)),'w')
	#for r in os.listdir(os.path.join(sys.argv[1],f)):
	#	data = open(os.path.join(sys.argv[1],f,r),'r')
	#	for line in data:
	#		if(line == ''):
	#			continue
	#		parts = line.split('\t')
	#		output.write(parts[0]+' '+parts[1]+'\n')

