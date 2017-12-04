def input(task):
    workfile = '{0}_input.txt'.format(task)
    f = open(workfile)
    try:
        return f.read()
    except FileNotFoundError:
        print("File not found")

        # matrix numbered like this:
        # _|___|___|___|__
        #  | 1 | 2 | 3 |
        #  | 4 | 5 | 6 |
        #  | 7 | 8 | 9 |

        # up means -3 value
        # while previous in (1,2,3) pass
        # down means +3 value
        # while previous in (7,8,9) pass
        # left means -1
        # while previous in (1,4,7) pass
        # right means +1
        # while previous in (3,6,8) pass


def move(input_string):
    currentNumber = 5
    storage = []
    moves = input_string.split('\n')
    for line in moves:
        for character in line:
            if character == 'U' and currentNumber not in (1, 2, 3):
                currentNumber -= 3
            elif character == 'D' and currentNumber not in (7, 8, 9):
                currentNumber += 3
            elif character == 'L' and currentNumber in (2, 3, 5, 6, 8, 9):
                currentNumber -= 1
            elif character == 'R' and currentNumber in (1, 2, 4, 5, 7, 8):
                currentNumber += 1
        storage.append(currentNumber)

    return storage


# Part 2 masterpiece numpad
#      1        ==>>       1
#    2 3 4      ==>>     2 3 4
#  5 6 7 8 9    ==>>   5 6 7 8 9
#    A B C      ==>>    10 11 12
#      D        ==>>      13

def move2(input_string):
    currentNumber = 5
    storage = []
    moves = input_string.split('\n')
    for line in moves:
        for character in line:
            if character == 'U' and currentNumber in (10, 11, 12, 6, 7, 8):
                currentNumber -= 4
            elif character == 'U' and currentNumber in (13, 3):
                currentNumber -= 2
            elif character == 'D' and currentNumber in (2, 3, 4, 6, 7, 8):
                currentNumber += 4
            elif character == 'D' and currentNumber in (1, 11):
                currentNumber += 2
            elif character == 'L' and currentNumber in (3, 4, 6, 7, 8, 9, 11, 12):
                currentNumber -= 1
            elif character == 'R' and currentNumber in (2, 3, 5, 6, 7, 8, 10, 11):
                currentNumber += 1
        storage.append(currentNumber)
        if currentNumber == 10:
            storage.append('A')
            storage.remove(10)
        if currentNumber == 11:
            storage.append('B')
            storage.remove(11)
        if currentNumber == 12:
            storage.append('C')
            storage.remove(12)
        if currentNumber == 13:
            storage.append('D')
            storage.remove(13)

    return storage


def solution():
    result = move(input('Task2'))
    print(result)


def solution2():
    result = move2(input('Task2'))
    print(result)


solution()
solution2()

"""

    |        '||''''|      .|'''.|     |''||''|    '||'  '||'    '||''''|   |''||''|    '||'      ..|'''.|
   |||        ||  .        ||..  '        ||        ||    ||      ||  .        ||        ||     .|'     '
  |  ||       ||''|         ''|||.        ||        ||''''||      ||''|        ||        ||     ||
 .''''|.      ||          .     '||       ||        ||    ||      ||           ||        ||     '|.      .
.|.  .||.    .||.....|    |'....|'       .||.      .||.  .||.    .||.....|    .||.      .||.     ''|....'

  """
