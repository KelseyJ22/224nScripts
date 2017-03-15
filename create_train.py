import os
import math

fnames = ['output_1.txt']

def process():
	dataset = list()
	for fname in fnames:
		f = open(fname, 'r')
		for line in f:
			split = line.split()
			if len(split) > 1: # success
				label = split[-2] # second to last (last = year; we want decade)
				if 'a' not in label:
					label = str(int(math.ceil(int(label) / 100.0)) * 100)
					string = split[:-2]
					dataset.append(str(string) + '\t' + label + '\n')

	o = open('train.conll', 'w')
	o.write('-DOCSTART-\tO\n\n')
	written = 0
	for line in dataset:
		if written < 1000000:
#			print 'writing ' + line
			o.write(line + '\n')
		written += 1
	o.close()
	f.close()

process()
