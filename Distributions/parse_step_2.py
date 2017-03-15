def initialize():
	distrib = {1800: 0, 1820: 0, 1840: 0, 1860: 0, 1880: 0, 1890: 0, 1900: 0, 1910: 0, 1920: 0, 1940: 0, 1960: 0, 1980: 0, 2000: 0, 'total': 0}
	return distrib


def add_to_distrib(bucket, count, distribution):
	distribution[int(bucket.strip())] += int(count.strip())
	distribution['total'] += int(count.strip())
	return distribution


def normalize(distrib):
	res = list()
	total = distrib['total']
	res.append(float(distrib[1800])/float(total))
	res.append(float(distrib[1820])/float(total))
	res.append(float(distrib[1840])/float(total))
	res.append(float(distrib[1860])/float(total))
	res.append(float(distrib[1880])/float(total))
	res.append(float(distrib[1900])/float(total))
	res.append(float(distrib[1920])/float(total))
	res.append(float(distrib[1940])/float(total))
	res.append(float(distrib[1960])/float(total))
	res.append(float(distrib[1980])/float(total))
	res.append(float(distrib[2000])/float(total))
	return res


def parse(filename, count):
	f = open(filename, 'r')
	o = open('distributions' + str(count) + '.txt', 'w')
	curr_sentence = ''
	distribution = initialize()
	for line in f:
		split = line.split('\t')
		if len(split) > 2:
			sentence = split[0]
			bucket = split[1]
			count = split[2]
			if sentence != curr_sentence:
				if distribution['total'] > 0: # done with current sentence
					distrib = normalize(distribution)
					o.write(str(sentence) + '\t' + str(distrib) + '\n')
					# reset
					sentence = ''
					distribution = initialize()
				else: # starting a new sentence
					curr_sentence = sentence
					distribution = add_to_distrib(bucket, count, distribution)
			else: # continuing same sentence
				distribution = add_to_distrib(bucket, count, distribution)


	f.close()
	o.close()

count = 0
for filename in ['parsed_step_1_1.txt', 'parsed_step_1_2.txt', 'parsed_step_1_3.txt', 'parsed_step_1_4.txt', 'parsed_step_1_5.txt', 'parsed_step_1_6.txt', 'parsed_step_1_7.txt', 'parsed_step_1_8.txt', 'parsed_step_1_9.txt']:
	count += 1
	parse(filename, count)