from collections import Counter


def input(task):
    workfile = '{0}_input.txt'.format(task)
    f = open(workfile)
    try:
        return f.read()
    except FileNotFoundError:
        print("File not found")


def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]


def leastCommon(lst):
    data = Counter(lst)
    return data.most_common()[-1][0]


def part1(input_string):
    most_common = []
    data = [[] for d in range(0, 8)]
    input_string = input_string.split('\n')
    for line in input_string:
        for i in range(0, 8):
            data[i] += line[i]
    for i in range(0, 8):
        most_common += Most_Common(data[i])
    return most_common


def part2(input_string):
    least_common = []
    data = [[] for d in range(0, 8)]
    input_string = input_string.split('\n')
    for line in input_string:
        for i in range(0, 8):
            data[i] += line[i]
    for i in range(0, 8):
        least_common += leastCommon(data[i])
    return least_common


def solver():
    print(part1(input('Task6')))


def solver2():
    print(part2(input('Task6')))


solver()
solver2()
