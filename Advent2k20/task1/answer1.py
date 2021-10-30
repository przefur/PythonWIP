#import csv
import math

with open("input1.txt", 'r') as f:
    lines = map(int, f.readlines())

def answer1(lines):
    for line in lines:
        for i in range(0, len(lines)):
            if line + lines[i] == 2020:
                return (line * lines[i])

def answer2(lines):
    for line in lines:
        for i in range(0, len(lines)):
            checksum = line + lines[i]
            for j in range(0, len(lines)):
                if checksum + lines[j] == 2020:
                    return(line * lines[i] * lines[j])

print(answer1(lines))
print(answer2(lines))
