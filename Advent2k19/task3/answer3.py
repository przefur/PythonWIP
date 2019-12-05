with open ('input3.txt', 'r') as f:
	read_data = f.read()
	read_data = read_data.split('\n')
	s1 = read_data[0]
	s2 = read_data[1]
	s1 = s1.split(',')
	s2 = s2.split(',')


def snake(input_string):
	NS = 0
	EW = 0
	NS2 = 0
	EW2 = 0
	positions1 = []
	positions2 = []
	manhattan = []
	for i in range(0, len(s1)):
		if s1[i][0] == 'R':
			for i in range(0, int(s1[i][1:])):
					EW += 1
					positions1.append([NS,EW])
		elif s1[i][0] == 'L':
			for i in range(0, int(s1[i][1:])):
					EW -= 1
					positions1.append([NS,EW])
		elif s1[i][0] == 'U':
			for i in range(0, int(s1[i][1:])):
					NS += 1
					positions1.append([NS,EW])
		elif s1[i][0] == 'D':
			for i in range(0, int(s1[i][1:])):
					NS -= 1
					positions1.append([NS,EW])

	for i in range(0, len(s2)):
		if s2[i][0] == 'R':
			for i in range(0, int(s2[i][1:])):
					EW2 += 1
					positions2.append([NS2,EW2])
		elif s2[i][0] == 'L':
			for i in range(0, int(s2[i][1:])):
					EW2 -= 1
					positions2.append([NS2,EW2])
		elif s2[i][0] == 'U':
			for i in range(0, int(s2[i][1:])):
					NS2 += 1
					positions2.append([NS2,EW2])
		elif s2[i][0] == 'D':
			for i in range(0, int(s2[i][1:])):
					NS2 -= 1
					positions2.append([NS2,EW2])

	first_set = set([tuple(X) for X in positions1])
	second_set = set([tuple(X) for X in positions2])	
	intersections = first_set & second_set

	for x in intersections:
		manhattan.append((abs(x[0]) + abs(x[1])))
	return min(manhattan)


def snake3(input_string):
	NS = 0
	EW = 0
	NS2 = 0
	EW2 = 0
	jumps =0
	jumps2 =0
	positions1 = []
	positions2 = []
	positionsAndJumps =[]
	positionsAndJumps2=[]
	for i in range(0, len(s1)):
		if s1[i][0] == 'R':
			for i in range(0, int(s1[i][1:])):
					EW += 1
					jumps +=1
					positions1.append([NS,EW])
					positionsAndJumps.append([(NS,EW), jumps])
		elif s1[i][0] == 'L':
			for i in range(0, int(s1[i][1:])):
					EW -= 1
					jumps +=1
					positions1.append([NS,EW])
					positionsAndJumps.append([(NS,EW), jumps])
		elif s1[i][0] == 'U':
			for i in range(0, int(s1[i][1:])):
					NS += 1
					jumps +=1
					positions1.append([NS,EW])
					positionsAndJumps.append([(NS,EW), jumps])
		elif s1[i][0] == 'D':
			for i in range(0, int(s1[i][1:])):
					NS -= 1
					jumps +=1
					positions1.append([NS,EW])
					positionsAndJumps.append([(NS,EW), jumps])

	for i in range(0, len(s2)):
		if s2[i][0] == 'R':
			for i in range(0, int(s2[i][1:])):
					EW2 += 1
					jumps2 +=1
					positions2.append([NS2,EW2])
					positionsAndJumps2.append([(NS2,EW2), jumps2])
		elif s2[i][0] == 'L':
			for i in range(0, int(s2[i][1:])):
					EW2 -= 1
					jumps2 +=1
					positions2.append([NS2,EW2])
					positionsAndJumps2.append([(NS2,EW2), jumps2])
		elif s2[i][0] == 'U':
			for i in range(0, int(s2[i][1:])):
					NS2 += 1
					jumps2 +=1
					positions2.append([NS2,EW2])
					positionsAndJumps2.append([(NS2,EW2), jumps2])
		elif s2[i][0] == 'D':
			for i in range(0, int(s2[i][1:])):
					NS2 -= 1
					jumps2 +=1
					positions2.append([NS2,EW2])
					positionsAndJumps2.append([(NS2,EW2), jumps2])

	first_set = set([tuple(X) for X in positions1])
	second_set = set([tuple(X) for X in positions2])	

	intersections = first_set & second_set
	manhattan = list(intersections)

	stuf1 =[]
	stuf2 =[]

	for i in range(0, len(manhattan)):
		for j in range(0, len(positionsAndJumps)):
			if manhattan[i] ==positionsAndJumps[j][0]:
				stuf1.append((positionsAndJumps[j][1]))

	for i in range(0, len(manhattan)):
		for j in range(0, len(positionsAndJumps2)):
			if manhattan[i] == positionsAndJumps2[j][0]:
				stuf2.append((positionsAndJumps2[j][1]))

	for i in range(0, len(stuf1)):
		stuf1[i] += stuf2[i]

	return min(stuf1)




print('Answer #3.1:')
print(snake(read_data))

print('Answer #3.1:')
print(snake3(read_data))




