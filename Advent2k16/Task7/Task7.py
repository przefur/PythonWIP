def input(task):
    workfile = '{0}_input.txt'.format(task)
    f = open(workfile)
    try:
        return f.read()
    except FileNotFoundError:
        print("File not found")


def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def abba_checker(input_string):
    x = 0
    z = 0
    i_s = input_string.split('\n')
    for line in i_s:
        a = findOccurences(line, '[')
        b = findOccurences(line, ']')
        for d in range(0, len(line) - 3):
            if line[d] != line[d + 1] and line[d + 1] == line[d + 2] and line[d + 2] != line[d + 3] and line[d] == line[
                        d + 3]:
                x += 1
                print(d)
                d += 100000000000000
                print(d)
                for i in range(0, len(a)):
                    for j in range(int(a[i]) + 1, int(b[i]) - 2):
                        if line[j] != line[j + 1] and line[j + 1] == line[j + 2] and line[j] == line[j + 3] and line[
                            j] == line[j + 3]:
                            z += 1
                            x -= 1
                break

    pass


print(abba_checker(input('Task7')))


def abbachecker_test2():
    text = 'abba[abba]abba'
    print(abba_checker(text))


def abbachecker_test3():
    text = 'abba'
    print(abba_checker(text))


def abbachecker_test4():
    text = 'abba[abba]'
    print(abba_checker(text))


def abbachecker_test5():
    text = 'abfba[abba]abba'
    print(abba_checker(text))


def abbachecker_test6():
    text = 'abfba[abba]abfba'
    print(abba_checker(text))


def abbachecker_test7():
    text = 'abfba[abvba]abba'
    print(abba_checker(text))


def abbachecker_test8():
    text = 'abfba[abvba]abbaabbaabbaabba'
    print(abba_checker(text))


def abbachecker_test():
    text = '1234567'
    for i in range(0, len(text) - 3):
        print(text[i])
        print(text[i + 1])
        print(text[i + 2])
        print(text[i + 3])
        print('XXXXXXXX')


# abbachecker_test()
abbachecker_test2()
abbachecker_test3()
abbachecker_test4()
abbachecker_test5()
abbachecker_test6()
abbachecker_test7()
abbachecker_test8()
