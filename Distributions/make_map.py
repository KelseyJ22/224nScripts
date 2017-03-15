def process(sentence):
	res = list()
	for elem in sentence.split(','):
		res.append(elem.strip().replace('[', '').replace(']', '').replace("'", '').replace('\'', ''))
	return res


def to_float(distribution):
	res = list()
	for elem in distribution.split(','):
		elem = elem.strip().replace('[', '').replace(']', '').replace("'", '').replace('\'', '')
		if len(elem) >= 1:
			res.append(float(elem))
	return res

def cleanup(ngram):
	res = list()
	for word in ngram:
		res.append(word.strip().lower().replace('\xe2\x80\x99', '\'').replace('\xe2\x80\x9c',"\'").replace('\xe2\x80\x9d', '\"').replace('[', '').replace(']', '').replace("'", '').replace('\'', ''))
	return res


def make_map():
	f = open('new_normalization_scheme.txt', 'r')
	ngram_to_distribution = dict()
	for line in f:
		split = line.split('\t')
		if len(split) == 2:
			ngram = process(split[0])
			label = to_float(split[1])
			ngram_to_distribution[str(ngram)] = label
	f.close()

	o = open('book_with_distributions.txt', 'w')
	f = file('book.txt').read()
	words = f.split()
	for i in range(0, len(words)):
		if i + 5 < len(words):
			ngram = cleanup(words[i:i + 5])
			if ngram in ngram_to_distribution:
				distribution = ngram_to_distribution[ngram]
			else:
				distribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
			o.write(ngram + '\t' + distribution + '\n')
	o.close()
	f.close()

make_map()