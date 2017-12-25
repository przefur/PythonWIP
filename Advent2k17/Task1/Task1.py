with open('Task1_input.txt', 'r') as f:
    read_data = f.read()


def captcha(input_string):
    total = 0
    for i in range(0, len(input_string)):
        if input_string[- 1 + i] == input_string[i]:
            total += (int(input_string[- 1 + i]))
    return total


def captcha2(input_string):
    c = int((len(input_string)) / 2)
    total2 = 0
    for i in range(0, 2 * c):
        if input_string[i - c] == input_string[i]:
            total2 += (int(input_string[i]))
    return total2


print(captcha(read_data))
print(captcha2(read_data))
