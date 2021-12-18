#!/usr/bin/env python3

import os
import numpy as np
from functools import reduce


class Board:
    def __init__(self, string_list):
        self.mark = np.zeros((5, 5))
        self.data = np.array([line.split() for line in string_list], dtype=int)
        self.finished = False

    def mark_number(self, number):
        self.mark[np.where(self.data == number)] = 1

    def check(self):
        return np.any((np.sum(self.mark, 0) == 5)) or np.any(np.sum(self.mark, 1) == 5)

    def isFinished(self):
        return self.finished

    def setFinished(self):
        self.finished = True

    def finallly(self):
        print(self.data)
        print(self.mark)
        return self.data[np.where(self.mark == 0)]

    def __repr__(self):
        return self.data.__repr__()


def first():
    for m in moves:
        for board in boards:
            board.mark_number(m)
            if board.check():
                result = board.finallly();
                return m * np.sum(result)


def second():
    notDoneBoards = n_boards
    for m in moves:
        for board in boards:
            board.mark_number(m)
            if not board.isFinished() and board.check() and notDoneBoards > 1:
                notDoneBoards -= 1
                board.setFinished()
            if notDoneBoards == 1 and not board.isFinished() and board.check():
                    result = board.finallly();
                    return m * np.sum(result)


if __name__ == '__main__':
    file = "input.txt"
    data = np.array([line.rstrip('\n') for line in open(file)])
    moves = [int(i) for i in data[0].split(',')]
    n_boards = int(len(data[1:]) / 6)
    boards = [Board(data[int(6 * i) + 2:int(6 * i) + 7]) for i in range(n_boards)]
    print(first())
    print(second())
    print(moves)
