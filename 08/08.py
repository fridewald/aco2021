#!/usr/bin/env python3
import os
from typing import Dict

import numpy as np


def first():
    count = 0
    for (tester, solve_it) in use_it:
        dict_it = dict()
        for code in tester:
            if (len(code) == 2):
                dict_it[1] = "".join(sorted(code))
            elif (len(code) == 3):
                dict_it[7] = ''.join(sorted(code))
            elif (len(code) == 4):
                dict_it[4] = ''.join(sorted(code))
            elif (len(code) == 7):
                dict_it[8] = "".join(sorted(code))
        easy = [dict_it[i] for i in [1, 4, 7, 8]]
        # print(dict_it[(1, 4, 7, 8)])
        for code in solve_it:
            if ''.join(sorted(code)) in easy:
                count += 1
    return count


def sorting(code):
    return ''.join(sorted(code))

def is_inside(to_check, to_be_in):
    return all([(f_st in to_be_in) for f_st in to_check])


def second():
    count = 0
    for (tester, solve_it) in use_it:
        dict_it: Dict[int, str] = dict()
        for code in tester:
            code = sorting(code)
            if (len(code) == 2):
                dict_it[1] = code
            elif (len(code) == 3):
                dict_it[7] = code
            elif (len(code) == 4):
                dict_it[4] = code
            elif (len(code) == 7):
                dict_it[8] = code
        # easy = [dict_it[i] for i in [1, 4, 7, 8]]
        for code in tester:
            code = sorting(code)
            if (len(code) == 6):
                if (is_inside(dict_it[4], code)):
                    dict_it[9] = code
                elif (is_inside(dict_it[1], code)):
                    dict_it[0] = code
                else:
                    dict_it[6] = code

        for code in tester:
            code = sorting(code)
            if (len(code) == 5):
                if (is_inside(dict_it[1], code)):
                    dict_it[3] = code
                elif (is_five(code, dict_it[4])):
                    dict_it[5] = code
                else:
                    dict_it[2] = code

        undict_it = dict()
        for(key, value) in dict_it.items():
            undict_it[value] = key

        # print(dict_it)
        # print(undict_it)

        solve_it = [sorting(sol) for sol in solve_it]
        thi_number = 0
        thi_number += 1e3*undict_it[solve_it[0]]
        thi_number += 1e2*undict_it[solve_it[1]]
        thi_number += 1e1*undict_it[solve_it[2]]
        thi_number += undict_it[solve_it[3]]
        count += thi_number
    return(int(count))

def is_five(code, code_4):
    count = 0
    for s in code_4:
        if s in code:
            count += 1
    return count == 3


if __name__ == '__main__':
    file = "input.txt"
    lines = [line.rstrip('\n') for line in open(file)]
    use_it = [(raw.split(' ')[0:10], raw.split(' ')[11:]) for raw in lines]
    # print(use_it)gcc
    print(first())
    # use_it = use_it[0:2]
    print(second())
