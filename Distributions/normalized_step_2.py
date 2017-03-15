import numpy as np

bucket_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

TOTAL = 11

def initialize():
	distrib = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	return distrib


def add_to_distrib(bucket, count, distribution):
	index = (int(bucket) - 1800)/20
	distribution[index] += int(count)
	return distribution


def normalize_by_bucket(distrib):
	result = list()
	for i in range(0, len(distrib)):
		curr_count = distrib[i]
		bucket_count = bucket_counts[i]
		if bucket_count > 0.0:
			result.append(float(curr_count)/float(bucket_count))
		else:
			result.append(0.0)
	return result


def total(distrib):
	res = 0.0
	for elem in distrib:
		elem = float(elem)
		res += elem
	return res

def norm(distrib, total):
	res = list()
	for elem in distrib:
		if total > 0:
			res.append(float(elem)/float(total))
		else:
			res.append(0)
	return res

def get_counts(filename):
	f = open(filename, 'r')
	counts = list()
	curr_sentence = ''
	distribution = initialize()
	for line in f:
		split = line.split('\t')
		if len(split) == 3:
			bucket = split[1].strip()
			count = split[2].strip()
			index = (int(bucket) - 1800)/20
			bucket_counts[index] += int(count)

			sentence = split[0].strip()
			bucket = split[1].strip()
			count = split[2].strip()

			if sentence != curr_sentence: # starting new sentence
				counts.append((curr_sentence, distribution)) # record previous
				distribution = initialize() # reset
				curr_sentence = sentence # new sentence
				distribution = add_to_distrib(bucket, count, distribution)
			else: # continuing same sentence
				distribution = add_to_distrib(bucket, count, distribution)

	counts.append((curr_sentence, distribution)) # last line of file

	f.close()
	counts = counts[1:]

	o = open('results.txt', 'w')
	for elem in counts:
		sentence = elem[0]
		distribution = elem[1]
		distrib = normalize_by_bucket(distribution)
		normalized = norm(distrib, total(distrib))
		o.write(sentence + '\t' + str(normalized) + '\n')
	o.close()


get_counts('random_split_1.txt')