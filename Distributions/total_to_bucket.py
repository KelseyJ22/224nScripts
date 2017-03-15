def convert(year):
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


def total_to_buckets():
	f = file('total_counts.txt').read()
	buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	split = f.split('\t')
	for elem in split:
		data = elem.split(',')
		if len(data) > 2:
			year = convert(data[0].strip())
			if year <= 2000 and year >= 1800:
				count = data[1].strip()
				index = (year - 1800)/20
				buckets[index] += int(count)

	o = open('bucket_counts.txt', 'w')
	for i in range(0, len(buckets)):
		year = (i * 20) + 1800
		o.write(str(year) + ' ' + str(buckets[i]) + '\n')

total_to_buckets()