with open('Task3_input.txt', 'r') as f:
    read_data = f.read()

import math


# each new outer-layer can be easily found by exponentiation of not-odd number
# first layer is 1^2 which is 1
# first layer is 3^2 which is 9
# first layer is 5^2 which is 25


def layer(input_string):
    s = float(input_string)
    x = math.ceil(math.sqrt(s))
    if int(math.ceil(math.sqrt(s))) % 2 == 0:
        x += 1
    return x


def height(input_string):
    s = float(input_string)
    corner_number = layer(input_string) * layer(input_string)
    rest = corner_number - s
    return (rest % ((layer(input_string) - 1) / 2))


def width(input_string):
    s = float(input_string)
    return int((layer(input_string) - 1) / 2)


def solution():
    return height(read_data) + width(read_data)


print(solution())


# defining important points:
# fist, second and third corner has 2 neighbours
# fourth corner has 3 neighbours
# fist in a player has only 2 neighbours
# every other in-between cell has 3 neighbours
# fist and second cell is 1


def solution2(input_string):
    pass
