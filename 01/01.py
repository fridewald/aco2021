#!/usr/bin/env python3

import os

file = "input.txt"

data = list()
data = [line.rstrip('\n') for line in open(file)]
increases = 0
count = 0
for last, current in zip(data, data[1:]):
    count += 1
    if(int(last) < int(current)):
        print("increase:", last, current)
        increases += 1
    else:
        print("decrease:", last, current)

print(increases)
print(count)
