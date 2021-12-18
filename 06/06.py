#!/usr/bin/env python3

import os
import numpy as np

def first():
    birthday = [0 for _ in range(7)]
    new_borns = [0, 0]
    for i in in_fish:
        birthday[i] += 1
    for day in range(256):
        now_adult = new_borns[day%2]
        new_borns[day%2] = birthday[day%7]
        birthday[day%7] += now_adult
    print(birthday)
    print(new_borns)
    return sum(birthday) + sum(new_borns)

if __name__ == '__main__':
    file = "input.txt"
    in_fish = [ line.rstrip('\n').split(',') for line in open(file)][0]
    in_fish = [int(i) for i in in_fish]
    print(in_fish)
    print(first())

