#!/usr/bin/env python3

import os

file = "input.txt"

data = [int(line.rstrip('\n')) for line in open(file)]
three_window = [data[i] + data[i+1] + data[i+2] for i in range(len(data)-2)]
increase_list = [1 for i in range(len(three_window)-1) if three_window[i] < three_window[i+1]]
print(sum(increase_list))
