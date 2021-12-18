#!/usr/bin/env python3
import os
import numpy as np

def first():
    max_crab = max(crabs)
    min_crab = min(crabs)
    fuel = [sum([abs(crab - i) for crab in crabs]) for i in range(min_crab, max_crab+1)]
    return min(fuel)

def second():
    max_crab = max(crabs)
    min_crab = min(crabs)
    fuel = [sum([abs(crab - i)*(abs(crab - i)+1)/2 for crab in crabs]) for i in range(min_crab, max_crab+1)]
    return min(fuel)

if __name__ == '__main__':
    file = "input.txt"
    crabs = [line.rstrip('\n').split(',') for line in open(file)][0]
    crabs = [int(i) for i in crabs]
    print(first())
    print(second())

