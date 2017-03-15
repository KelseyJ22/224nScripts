def process_ngram(ngram):
	res = list()
	for word in ngram:
		index = word.find('_')
		if index != -1:
			word = word[:index]
		res.append(word)
	return str(res)

def split_dataset():
	i = 26
	while i < 50:
		for j in range(i, i+5):
			fname = 'parsed_' + str(j) + '.txt'
			print 'reading ' + fname + '\n'
			f = open(fname, 'r')
			ngrams = dict()
			for line in f:
				split = line.split('\t')
				if len(split) == 2:
					ngram = split[0]
					split_ngram = ngram.split(',')
					if len(split_ngram) == 5: # only store properly formed ngrams
						label = int(split[1].rstrip())
						ngram = process_ngram(split_ngram)
						if ngram in ngrams:
							if label in ngrams[ngram]:
								ngrams[ngram][label] += 1
							else:
								ngrams[ngram][label] = 1
							ngrams[ngram]['total'] += 1
						else:
							ngrams[ngram] = {label: 1, 'total': 1}

			f.close()

		o = open('distributions_' + str(i/5) + '.txt', 'w')
		for ngram in ngrams:
			distrib = list()
			for label in ['1800', '1820', '1840', '1860', '1880', '1900', '1920', '1940', '1960', '1980', '2000']:
				if int(label) in ngrams[ngram]:
					distrib.append(float(ngrams[ngram][int(label)])/float(ngrams[ngram]['total']))
				else:
					distrib.append(0.0)

			#print str(ngram) + '\t' + str(distrib) + '\n'
			o.write(str(ngram) + '\t' + str(distrib) + '\n')
		o.close()

		i += 5


split_dataset()