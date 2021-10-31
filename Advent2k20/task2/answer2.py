with open("input2.txt", 'r') as f:
    lines = f.readlines()
    
    
    
def prep(input_string):
    clean = []
    for line in lines:
        split = line.split()
        
        check = split[0]
        check = check.split("-")
        first = int(check[0])
        second = int(check[1])
        
        character = split[1][0]
        
        chain = split[2]
        
        clean.append([first, second, character, chain])
        
    return clean
    

def answer1(clean):
    counter = 0

    for i in range(0, len(clean)):
        if clean[i][3].count(clean[i][2]) in range (clean[i][0], clean[i][1] + 1):
            counter += 1

    return counter

def answer2(clean):
    counter = 0
    for i in range(0, len(clean)):
        if (clean[i][3][clean[i][0] - 1] == clean[i][2] and clean[i][3][clean[i][1] - 1] != clean[i][2]) or (clean[i][3][clean[i][0] - 1] != clean[i][2] and clean[i][3][clean[i][1] - 1] == clean[i][2]):
            counter += 1
    return counter


print(answer1(prep(lines)))
print(answer2(prep(lines)))



