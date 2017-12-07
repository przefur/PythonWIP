import re
import string
from collections import Counter


def input(task):
    workfile = '{0}_input.txt'.format(task)
    f = open(workfile)
    try:
        return f.read()
    except FileNotFoundError:
        print("File not found")


def part1(input_string):
    total = 0
    splitparts = re.compile(r'([a-z-]+)(\d+)\[(.+)\]')
    roomsList = input_string.split('\n')
    for room in roomsList:
        roomCode = splitparts.findall(room)
        clean_room_code = roomCode[0][0].replace('-', '')
        clean_room_code = Counter(clean_room_code)
        clean_room_serialCode = int(roomCode[0][1])
        clean_room_checkCode = roomCode[0][2]
        most = ''.join(k for (k, v) in sorted(clean_room_code.most_common(), key=lambda k: (-k[1], k[0])))
        if most.startswith(clean_room_checkCode):
            total += int(clean_room_serialCode)
    return total


def part2(input_string):
    splitparts = re.compile(r'([a-z-]+)(\d+)\[(.+)\]')
    roomsList = input_string.split('\n')
    alphabet = string.ascii_lowercase
    for room in roomsList:
        roomCode = splitparts.findall(room)
        clean_room_code = roomCode[0][0]
        clean_room_serialCode = int(roomCode[0][1])
        table = str.maketrans(alphabet, alphabet[clean_room_serialCode % 26:] + alphabet[0: clean_room_serialCode % 26])
        if clean_room_code.translate(table) == 'northpole-object-storage-':
            return clean_room_serialCode



            # for i in range (0, len(table), 5):
            #    querry += [(table[i:i+5])]
            # for i in range (0, len(querry)):
            #    number1 = int(querry[0][0][1])
            #    number2 = int(querry[0][1][1])
            #    number3 = int(querry[0][2][1])
            #    number4 = int(querry[0][3][1])
            #    number5 = int(querry[0][4][1])
            #    if number1 == number2 or number2 == number3 or number3 == number4 or number4 == number5:
            #    if string.ascii_lowercase.index(str(querry[0][1][0])) >= string.ascii_lowercase.index(str(querry[0][2][0])):
            #        a = querry[0][1][0]
            #        b = querry[0][2][0]
            #        querry[0][1][0] = b
            #        querry[0][2][0] = a


#

def solver():
    print(part1(input('Task4')))


def solver2():
    print(part2(input('Task4')))


solver()
solver2()
