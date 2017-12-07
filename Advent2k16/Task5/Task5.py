import hashlib
import string


def input(task):
    workfile = '{0}_input.txt'.format(task)
    f = open(workfile)
    try:
        return f.read()
    except FileNotFoundError:
        print("File not found")


def part2(input_string):
    i = 0
    password = []
    position = []
    desired_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    alphabet = string.ascii_lowercase
    while len(password) < 8:
        m = hashlib.md5((input_string + str(i)).encode('utf-8')).hexdigest()
        if m[5] in alphabet:
            pass
        elif str(m).startswith('00000') and int(m[5]) in desired_positions:
            password += m[5]
            position += m[6]
            desired_positions.remove(int(m[5]))
        i += 1

    return password, position


def part1(input_string):
    i = 0
    password = []
    while len(password) < 8:
        m = hashlib.md5((input_string + str(i)).encode('utf-8')).hexdigest()
        if str(m).startswith('00000'):
            password += m[5]
        i += 1
    return password


def desired_position_test():
    desired_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(0, 6):
        desired_positions.remove(i)
    print(desired_positions)


def solver():
    print(part1(input('Task5')))


def solver2():
    print(part2(input('Task5')))


solver()
solver2()
desired_position_test()
