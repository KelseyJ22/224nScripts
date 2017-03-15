
def process_ngram(ngram):
	res = list()
	for word in ngram:
		res.append(word.strip().lower().replace('\xe2\x80\x99', '\'').replace('\xe2\x80\x9c',"\'").replace('\xe2\x80\x9d', '\"'))
	return res

f = file('book.txt').read()
words = f.split()
for i in range(0, len(words)):
	if i+5 < len(words):
		ngram = words[i:i+5]
		ngram = process_ngram(ngram)
		print ngram