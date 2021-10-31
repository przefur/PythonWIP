with open("input3.txt", 'r') as f:
    lines = f.readlines()
    lines.pop(0)


def answer1(input):

    interval = 0
    trees = 0
    for line in lines:
        interval += 3
        if line[interval % 31] == '#':
            trees += 1
    return trees

def answer2(input):

    interval1 = 0
    interval2 = 0
    interval3 = 0
    interval4 = 0
    interval5 = 0
    linenum = 1
    
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0

    for line in lines:
        interval1 += 1
        interval2 += 3
        interval3 += 5
        interval4 += 7
        if line[interval1 % 31] == '#':
            t1 += 1
        if line[interval2 % 31] == '#':
            t2 += 1
        if line[interval3 % 31] == '#':
            t3 += 1
        if line[interval4 % 31] == '#':
            t4 += 1
        if linenum % 2 == 0:
            interval5 += 1
            if line[interval5 % 31] == '#':
                t5 += 1
        linenum += 1
            
        
            
    return t1, t2, t3, t4, t5, t1 * t2 * t3 * t4 * t5

print(answer1(lines))
print(answer2(lines))
