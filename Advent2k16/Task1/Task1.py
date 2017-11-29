def input(task):
    workfile = '{0}_input.txt'.format(task)
    f = open(workfile)
    try:
        return f.read()
    except FileNotFoundError:
        print("File not found")


def rotate(l, n):
    return l[-n:] + l[:-n]


def distance(end_position):
    dd = abs(end_position[0]) + abs(end_position[1])
    return dd


def movement(input_string):
    listOfPositions = set()
    listOfDirections = ['N', 'E', 'S', 'W']  # can be done on desq, but lists are fun too
    currentDirection = listOfDirections[0]
    end_position = [0, 0]
    positionVisitedTwice = ()
    input_list = input_string.split(', ')

    def positionVisited():
        nonlocal positionVisitedTwice
        if not positionVisitedTwice:
            current_position = tuple(end_position)
            if current_position in listOfPositions:
                positionVisitedTwice = current_position
            else:
                listOfPositions.add(current_position)

    for i in input_list:
        i = i.strip()
        turn, strides = i[0], int(i[1:])

        if turn == 'R':
            listOfDirections = rotate(listOfDirections, -1)
        else:
            listOfDirections = rotate(listOfDirections, 1)
        currentDirection = listOfDirections[0]

        for i in range(strides):

            if currentDirection == 'N':
                end_position[1] += 1
            elif currentDirection == 'E':
                end_position[0] += 1
            elif currentDirection == 'S':
                end_position[1] -= 1
            else:
                end_position[0] -= 1

            positionVisited()

    print(positionVisitedTwice)
    return end_position


def rotate_test():
    listOfDirections = ['N', 'E', 'S', 'W']
    assert (rotate(listOfDirections, 1) == ['W', 'N', 'E', 'S'])
    assert (rotate(listOfDirections, -1) == ['E', 'S', 'W', 'N'])


def movement_test():
    test_input = "R3, R2, R2, R2"
    end_pos = movement(test_input)
    dist = distance(end_pos)
    assert dist == 1


def distance_test():
    pointOfInterest = [4, 6]
    result = distance(pointOfInterest)
    assert result == 10


def solution():
    end_pos = movement(input('Task1'))
    dd = distance(end_pos)
    print('Result: ', dd)


rotate_test()
movement_test()
distance_test()
solution()
