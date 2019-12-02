#import csv
import math

with open("input1.txt", 'r') as f:
	read_data = f.read()
#	reader = csv.reader(f, delimiter='\t')



def adder(input_string):
	s = input_string.split('\n')
	total = 0
	for line in s:
		line_float = float(line)
		sb = int(math.floor(line_float / 3)) - 2
		total += sb
	return total

def adder2(input_string):
	s = input_string.split('\n')
	total = 0
	for line in s:
		line_float = float(line)
		sb = int(math.floor(line_float / 3)) - 2
		total += sb
		while sb > 0:
			sb = int(math.floor(sb / 3)) - 2
			if sb < 0:
				break
			else:
				total += sb
	return total



print('Answer #1.1:')
print(adder(read_data))

print('Answer #1,2:')
print(adder2(read_data))