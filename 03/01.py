#!/usr/bin/env python3

import os
import numpy as np
from functools import reduce

file = "input.txt"

data = np.array([line.rstrip('\n') for line in open(file)])
bit_length = len(data[0])
data_length = len(data)
common_array = [0 for _ in range(bit_length)]
print(common_array)
for line in data:
    for i, bit in enumerate(line):
        if bit == '0':
            common_array[i] -= 1
        elif bit == '1':
            common_array[i] += 1
print(common_array)

gamma = 0
for co in common_array:
    gamma = gamma << 1
    if co > 0:
        gamma += 1
    elif co == 0:
        print('Something fishy')

epsilon = (gamma^(2**(bit_length)-1))
print(f"Gamma   {gamma:>08b}")
print(f"Epilson {epsilon:>08b}")
print(f"Power {gamma*epsilon:>08b}")
print(f"Power {gamma*epsilon}")


# second
most_co_data = np.array([[int(i) for i in line] for line in data])
for bit_i in range(bit_length):
    if len(most_co_data) == 1:
        break
    most_common = -((len(most_co_data)+1)//2) + sum(most_co_data[:,bit_i])
    if most_common >= 0:
        most_common = 1
    else:
        most_common = 0
    most_co_data = np.array([dat for dat in most_co_data if dat[bit_i]==most_common])
oxy = reduce(lambda a, b: ((a<<1) + b), most_co_data[0])
print(f"Oxy:\t\t{oxy}")
print(f"Oxy:\t\t{oxy:>08b}")

lest_co_data = np.array([[int(i) for i in line] for line in data])
for bit_i in range(bit_length):
    if len(lest_co_data) == 1:
        break
    lest_common = -(len(lest_co_data+1))//2 + sum(lest_co_data[:,bit_i])
    if lest_common >= 0:
        lest_common = 0
    else:
        lest_common = 1
    lest_co_data = np.array([dat for dat in lest_co_data if dat[bit_i]==lest_common])
co2 = reduce(lambda a, b: ((a<<1) + b), lest_co_data[0])
print(f"CO2:\t\t{co2}")
print(f"CO2:\t\t{co2:>08b}")

print(f"Life support:\t{co2*oxy}")
