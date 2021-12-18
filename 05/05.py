#!/usr/bin/env python3

import os
import numpy as np

def first():
    floor = np.zeros((1000, 1000))
    for line in lines:
        x1= line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        if y1==y2:
            floor[min(x1, x2):max(x1,x2)+1,  y1] += 1
        elif x1==x2:
            floor[x1, min(y1,y2):max(y1,y2)+1] += 1
    return len(np.where(floor >= 2)[0])

def second():
    floor = np.zeros((1000, 1000))
    for line in lines:
        x1= line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        if y1==y2:
            floor[min(x1, x2):max(x1,x2)+1,  y1] += 1
        elif x1==x2:
            floor[x1, min(y1,y2):max(y1,y2)+1] += 1
        else:
            floor[make_diagonal(x1, y1, x2, y2)] += 1
    return len(np.where(floor >= 2)[0])

def make_diagonal(x1, y1, x2, y2):
    signx = (x2-x1)/np.abs(x1-x2)
    signy = (y2-y1)/np.abs(y1-y2)
    all = ([(int(x1+signx*i), int(y1+signy*i)) for i in range(np.abs(x1-x2)+1)])
    x = ([a[0] for a in all], [b[1] for b in all])
    return x


def decode_lines(line):
    (x1, y1x2, y2) = line.split(',')
    (y1, x2) = y1x2.split(' -> ')
    return (int(x1), int(y1)), (int(x2), int(y2))

if __name__ == '__main__':
    file = "input.txt"
    data = np.array([line.rstrip('\n') for line in open(file)])
    lines = [decode_lines(entry) for entry in data]
    # print(lines)
    print(f"At at least {first()} places two lines overlap.")
    # lines = lines[0:1]
    print(lines)
    print(second())
