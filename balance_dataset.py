import math
import random

def balance_dataset():
	f = open('output_0.txt', 'r')
	labels = dict()
	for line in f:
		split = line.split('\t')
		if len(split) > 2:
			ngram = split[0]
			label = split[1].rstrip()
			label = str(int(math.ceil(int(label) / 100.0)) * 100)
			if label in labels:
				labels[label].append(ngram)
			else:
				labels[label] = list(ngram)
	f.close()

	test = open('test_med.conll', 'w')
	train = open('train_med.conll', 'w')
	dev = open('dev_med.conll', 'w')

	for label in ['1800', '1900', '2000', '2100']:
		written_test = 0
		written_train = 0
		written_dev = 0

		while(written_test) < 100:
			ngram = random.choice(labels[label])
			sentence = ngram.split(' ')
			test.write(str(sentence) + '\t' + label + '\n')
			written_test += 1
		while(written_train) < 10000:
			ngram = random.choice(labels[label])
			sentence = ngram.split(' ')
			train.write(str(sentence) + '\t' + label + '\n')
			written_train += 1
		while(written_dev) < 100:
			ngram = random.choice(labels[label])
			sentence = ngram.split(' ')
			dev.write(str(sentence) + '\t' + label + '\n')
			written_dev += 1

	test.close()
	train.close()
	dev.close()

balance_dataset()
