with open('Task2_input.txt', 'r') as f:
    read_data = f.read()


def comparision(input_string):
    s = input_string.split('\n')
    checksum = 0
    for line in s:
        values = line.split('\t')
        values2 = [int(s) for s in values]
        checksum += max(values2) - min(values2)
    return checksum


def comparision2(input_string):
    s = input_string.split('\n')
    checksum = 0
    for line in s:
        values = line.split('\t')
        values2 = sorted([int(s) for s in values], reverse=True)
        i = 0
        for i, a in enumerate(values2):
            j = 0
            for j, b in enumerate(values2):
                if i != j and a % b == 0:
                    checksum += int(a / b)

    return checksum


print(comparision(read_data))
print(comparision2(read_data))
