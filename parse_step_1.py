import os

def process_sentence(raw):
	sentence = raw.split(' ')
	res = list()
	for word in sentence:
		word = word.strip()
		index = word.find('_')
		if index != -1:
			word = word[:index]
		res.append(word)
	return res

def convert_year(year):
	year_int = int(year)
	result = year_int
	if 1781 <= year_int <= 1800:
		result = 1800
	elif 1801 <= year_int <= 1820:
		result = 1820
	elif 1821 <= year_int <= 1840:
		result = 1840
	elif 1841 <= year_int <= 1860:
		result = 1860
	elif 1861 <= year_int <= 1880:
		result = 1880
	elif 1881 <= year_int <= 1900:
		result = 1900
	elif 1901 <= year_int <= 1920:
		result = 1920
	elif 1921 <= year_int <= 1940:
		result = 1940
	elif 1941 <= year_int <= 1960:
		result = 1960
	elif 1961 <= year_int <= 1980:
		result = 1980
	elif 1981 <= year_int <= 2000:
		result = 2000
	else:
		pass
	return result



def parse():
	o = open('parsed_step_1.txt', 'w')
	for filename in os.listdir(os.getcwd()):
		if '.py' not in filename:
			if filename != '.DS_Store':
				f = open(filename, 'r')
				print filename
				curr_bucket = 1800
				count = 0
				curr_sentence = ''
				for line in f:
					split = line.split('\t')

					sentence = process_sentence(split[0])
					year = split[1]
					occurences = split[2]

					if int(year.strip()) > 1780 and int(year.strip()) < 2001:  # if valid year
						bucket = convert_year(year)
						if sentence != curr_sentence:  # if new sentence
							o.write(str(curr_sentence) + '\t' + str(curr_bucket) + '\t' + str(count) + '\n')
							curr_sentence = sentence
							curr_bucket = 1800
							count = 0
						if bucket != curr_bucket:  # if new bucket
							if count > 0:
								o.write(str(curr_sentence) + '\t' + str(curr_bucket) + '\t' + str(count) + '\n')
							curr_bucket = bucket
							count = 0

						count += int(occurences)
					else:
						continue



parse()