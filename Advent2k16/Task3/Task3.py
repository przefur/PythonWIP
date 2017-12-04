def input(task):
    workfile = '{0}_input.txt'.format(task)
    f = open(workfile)
    try:
        return f.read()
    except FileNotFoundError:
        print("File not found")


def triangle(len1, len2, len3):
    if len1 + len2 > len3 and len1 + len3 > len2 and len2 + len3 > len1:
        return True
    else:
        return False


def checker(input_string):
    z = 0
    moves = input_string.split('\n')
    for line in moves:
        val = line.split()
        a = int(val[0])
        b = int(val[1])
        c = int(val[2])
        if triangle(a, b, c):
            z += 1
    return z


def checker2(input_string):
    asap = []
    akat = []
    akta = []
    z = 0
    moves = input_string.split('\n')
    for line in moves:
        val = line.strip()
        val2 = val.split()
        asap.append(val2[0])
        akat.append(val2[1])
        akta.append(val2[2])

    for i in range(0, len(asap), 3):
        if triangle(int(asap[i]), int(asap[i + 1]), int(asap[i + 2])):
            z += 1
        if triangle(int(akat[i]), int(akat[i + 1]), int(akat[i + 2])):
            z += 1
        if triangle(int(akta[i]), int(akta[i + 1]), int(akta[i + 2])):
            z += 1

    return z


def triangle_test():
    assert (triangle(3, 4, 5))


def checker_test():
    assert (checker('3 4 5'
                    '\n'
                    '4 8 7'))


def solver():
    print(checker(input('Task3')))


def solver2():
    print(checker2(input('Task3')))


triangle_test()
checker_test()
solver()
solver2()
