from collections import Counter

with open("input6.txt", 'r') as f:
    input_string = f.readlines()

def split(word):
    return [char for char in word]

def answerGetter(input_string):
    answer = []
    listofanswers = []
    for line in input_string:
        if line != "\n":
            line = split(line.rstrip())
            for element in line:
                answer.append(element)
        else:
            listofanswers.append(answer)
            answer = []
    listofanswers.append(answer)
    
    return listofanswers
    
    
def answerAndResponderGetter(input_string):
    responder = 0
    answer = []
    listofanswers = []
    for line in input_string:
        if line != "\n":
            responder +=1
            line = split(line.rstrip())
            for element in line:
                answer.append(element)
        else:
            listofanswers.append([answer, responder])
            answer = []
            responder = 0
    listofanswers.append([answer, responder])
    
    return listofanswers
    
    
def answer1(listofanswers):
    count = 0
    for answer in listofanswers:
        answer = set(answer)
        count += len(answer)
    return count

def answer2(listofanswers):
    count = 0
    my_dict = {}
    for answer in listofanswers:
        charlist = answer[0]
        maxval = answer[1]
        my_dict = {i:charlist.count(i) for i in charlist}
        for key in my_dict:
            if my_dict[key] == maxval:
                count += 1
    return count
    
    
print(answer1(answerGetter(input_string)))
print(answer2(answerAndResponderGetter(input_string)))
