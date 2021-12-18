#!/usr/bin/env python3

import os

file = "input.txt"

data = [line.rstrip('\n') for line in open(file)]
hori = depth = aim = 0
for line in data:
    move, number = line.split(' ')
    number = int(number)
    if(move == 'forward'):
        hori += number
        depth += number*aim
    elif(move == 'down'):
        aim += number
    elif(move == 'up'):
        aim -= number
    print(aim)

print(hori)
print(depth)
print(hori*depth)
