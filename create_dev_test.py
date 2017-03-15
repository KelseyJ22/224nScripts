import math

def process():
        f = open('output_0.txt', 'r')
        dataset = list()
        for line in f:
                split = line.split()
                if len(split) > 1: # success
                        label = split[-2] # second to last (last = year; we want decade)
			label = str(int(math.ceil(int(label) / 100.0)) * 100)
                        string = split[:-2]
#                        print label
			dataset.append(str(string) + '\t' + label + '\n')


        test = open('test.conll', 'w')
        dev = open('dev.conll', 'w')
        test.write('_DOCSTART-\tO\n\n')
        dev.write('-DOCSTART-\tO\n\n')
        count = 0
        written_dev = 0
        written_test = 0
        for line in dataset:
            if count % 2 == 0:
            	if written_test < 100000:
                	test.write(line + '\n')
                	written_test += 1
            else:
            	if written_dev < 100000:
                    dev.write(line + '\n')
                    written_dev += 1
            count += 1
        test.close()
        dev.close()
        f.close()

process()
