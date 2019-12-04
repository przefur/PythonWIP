with open ('input2.txt', 'r') as f:
	read_data = f.read()

def jumper(input_string):
	input_string = input_string.split(',')
	input_string = list(map(int, input_string))
	input_string[1] = 12
	input_string[2] = 2

	for i in range(0, len(input_string), 4):
		if input_string[i] == 1:
			input_string[input_string[i+3]] = input_string[input_string[i+1]] + input_string[input_string[i+2]]
		elif input_string[i] == 2:
			input_string[input_string[i+3]] = input_string[input_string[i+1]] * input_string[input_string[i+2]]
		elif input_string[i] == 99:
			break
	return input_string[0]

def jumper2(input_string):
	input_string = input_string.split(',')
	input_string = list(map(int, input_string))
	for x in range(0, 100):
		for y in range(0, 100):
			iss = list(input_string)
			iss[1] = x
			iss[2] = y

			for i in range(0, len(iss), 4):
				if iss[i] == 1:
					iss[iss[i+3]] = iss[iss[i+1]] + iss[iss[i+2]]
				elif iss[i] == 2:
					iss[iss[i+3]] = iss[iss[i+1]] * iss[iss[i+2]]
				elif iss[0] == 19690720:
					return (iss[1] * 100 + iss[2])
				elif iss[i] == 99:
					break

print('Answer #2.1:')
print(jumper(read_data))

print('Answer #2.2:')
print(jumper2(read_data))