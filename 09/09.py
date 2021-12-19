#!/usr/bin/env python3
import os
from functools import reduce
from typing import Dict

import numpy as np


def first():
    r = 0
    with_f = len(floor[0])
    height_f = len(floor)
    for i, line in enumerate(floor):
        for j, char in enumerate(line):
            if (i > 0 and char >= floor[i - 1][j]):
                continue
            if (i < height_f-1 and char >= floor[i + 1][j]):
                continue
            if (j > 0 and char >= floor[i][j - 1]):
                continue
            if (j < with_f-1 and char >= floor[i][j + 1]):
                continue
            # print(char)
            r += char + 1
    return r

def second():
    basi_sizes = list()
    with_f = len(floor[0])
    height_f = len(floor)
    indis = list((i, j) for j in range(with_f) for i in range(height_f))
    marked = set()

    def check(i, j):
        if floor[i][j] != 9 and (i, j) not in marked:
            return(find_field(i, j))
        else:
            return 0


    def find_field(i, j):
        if (floor[i][j] == 9):
            return 0
        field_size = 1
        marked.add((i,j))
        if (i > 0):
            field_size += check(i-1, j)
        if (i < height_f-1):
            field_size += check(i+1, j)
        if (j > 0):
            field_size += check(i, j-1)
        if (j < with_f-1):
            field_size += check(i, j+1)
        return field_size

    for ind in indis:
        f_size = find_field(*ind)
        if f_size == 0:
            continue
        basi_sizes.append(f_size)

    return(reduce(lambda x, y: x*y, sorted(basi_sizes, reverse=True)[0:3]))




if __name__ == '__main__':
    file = "input.txt"
    lines = [line.rstrip('\n') for line in open(file)]
    line_len = len(lines[0]);
    floor = [[int(character) for character in line] for line in lines]#[0:4]
    print(first())
    print(second())
    # use_it = use_it[0:2]
