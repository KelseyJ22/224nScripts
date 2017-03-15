import random

files = ['parsed_step_1_1.txt', 'parsed_step_1_2.txt', 'parsed_step_1_3.txt', 'parsed_step_1_4.txt', 'parsed_step_1_5.txt', 'parsed_step_1_6.txt', 'parsed_step_1_7.txt', 'parsed_step_1_8.txt', 'parsed_step_1_9.txt']

def initialize():
	output = list()
	for i in range(0, 11):
		output.append(open('random_split_' + str(i) + '.txt', 'w'))
	return output

def parse():
	output_files = initialize()
	for file in files:
		f = open(file, 'r')
		print 'reading from ' + file
		for line in f:
			index = random.randint(0, len(output_files)-1)
			output_files[index].write(line)

		f.close()

	for i in range(0, len(output_files)-1):
		output_files[i].close()

parse()