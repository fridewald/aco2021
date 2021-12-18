#!/usr/bin/env python3

import os

file = "input.txt"

data = [line.rstrip('\n') for line in open(file)]
forward = list()
down = list()
up = list()
for line in data:
    move, number = line.split(' ')
    number = int(number)
    if(move == 'forward'):
        forward.append(number)
    elif(move == 'down'):
        down.append(number)
    elif(move == 'up'):
        up.append(number)

hori = sum(forward)
depth = sum(down) - sum(up)
print(hori)
print(depth)
print(hori*depth)
