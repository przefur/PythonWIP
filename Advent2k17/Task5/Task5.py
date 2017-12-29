with open('Task5_input.txt', 'r') as f:
    data = f.read()


def mazejumper(input_string):
    s = input_string.split('\n')
    i = 0
    step = 0
    s2 = [int(x) for x in s]
    while i in range(0, len(s2)):
        current_position = s2[i]
        step += 1
        s2[i] += 1
        i += current_position

    return step


def mazejumper2(input_string):
    s = input_string.split('\n')
    i = 0
    step = 0
    s2 = [int(x) for x in s]
    while i in range(0, len(s2)):
        current_position = s2[i]
        step += 1
        if s2[i] >= 3:
            s2[i] -= 1
        else:
            s2[i] += 1
        i += current_position

    return step


print(mazejumper(data))
print(mazejumper2(data))
