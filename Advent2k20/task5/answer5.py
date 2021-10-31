with open("input5.txt", 'r') as f:
    input_string = f.readlines()

#FFFFBBBBLLLR
# vertical orientation : 128 rows (0 - 127)
# horizontal orientation : 8 rows (0 0 7)
# front - top half
# back - bottom half


def answer1(input_string):
    highestvalue = 0
    for line in input_string:
        verticalRow = list(xrange(128))
        horizontalRow = list(xrange(8))
        line = line.rstrip()
        verticalInstructions = line[:-3]
        horizontalInstructions = line[-3:]
        
        for i in range(0, len(verticalInstructions)):
            if verticalInstructions[i] == 'F':
                verticalRow = verticalRow[:len(verticalRow)/2]
            elif verticalInstructions[i] == 'B':
                verticalRow = verticalRow[len(verticalRow)/2:]
        
        for i in range(0, len(horizontalInstructions)):
            if horizontalInstructions[i] == 'L':
                horizontalRow = horizontalRow[:len(horizontalRow)/2]
            if horizontalInstructions[i] == 'R':
                horizontalRow = horizontalRow[len(horizontalRow)/2:]
                
        if 8 * int(verticalRow[0]) + int(horizontalRow[0]) > highestvalue:
            highestvalue = 8 * verticalRow[0] + horizontalRow[0]
        
    return highestvalue
    
    
def answer2(input_string):
    listOfValues = []
    listOfAllValues = []
    for line in input_string:
        verticalRow = list(xrange(128))
        horizontalRow = list(xrange(8))
        line = line.rstrip()
        verticalInstructions = line[:-3]
        horizontalInstructions = line[-3:]
        
        for i in range(0, len(verticalInstructions)):
            if verticalInstructions[i] == 'F':
                verticalRow = verticalRow[:len(verticalRow)/2]
            elif verticalInstructions[i] == 'B':
                verticalRow = verticalRow[len(verticalRow)/2:]
        
        for i in range(0, len(horizontalInstructions)):
            if horizontalInstructions[i] == 'L':
                horizontalRow = horizontalRow[:len(horizontalRow)/2]
            if horizontalInstructions[i] == 'R':
                horizontalRow = horizontalRow[len(horizontalRow)/2:]
                
        listOfValues.append(int(8 * int(verticalRow[0]) + int(horizontalRow[0])))
        listOfValues.sort()
        
    for x in range (128):
        for y in range(8):
            listOfAllValues.append(8 * x + y)
            
    experimental = [item for item in listOfAllValues if item not in listOfValues]
    
    for i in range (0, len(experimental)):
        if 15 <= experimental[i] <= answer1(input_string):
            x = experimental[i]
        
    return x
    
print(answer1(input_string))
print(answer2(input_string))
