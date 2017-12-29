with open('Task4_input.txt', 'r') as f:
    data = f.read()


def passphrase(input_string):
    s = input_string.split('\n')
    checksum = 0
    dd = []
    for line in s:
        s2 = line.split(' ')
        for i in range(0, len(s2)):
            dd.append(s2[i])
        if len(set([x for x in dd if dd.count(x) > 1])) > 0:
            checksum += 0
        else:
            checksum += 1
        dd = []
    return checksum


def passphrase2(input_string):
    s = input_string.split('\n')
    checksum = 0
    dd = []
    for line in s:
        s2 = line.split(' ')
        for i in range(0, len(s2)):
            dd.append(''.join(sorted(s2[i])))
        if len(set([x for x in dd if dd.count(x) > 1])) > 0:
            checksum += 0
        else:
            checksum += 1
        dd = []
    return checksum


print(passphrase(data))
print(passphrase2(data))
