#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
import numpy as np


class SudokuGenerater:
    def __init__(self):
        self.base_result = np.array([
            [7, 1, 2, 9, 8, 4, 3, 5, 6],
            [5, 3, 4, 1, 6, 7, 2, 8, 9],
            [9, 6, 8, 3, 5, 2, 7, 1, 4],
            [2, 8, 1, 5, 3, 9, 6, 4, 7],
            [6, 7, 3, 2, 4, 1, 5, 9, 8],
            [4, 5, 9, 6, 7, 8, 1, 2, 3],
            [8, 4, 5, 7, 2, 6, 9, 3, 1],
            [1, 2, 6, 4, 9, 3, 8, 7, 5],
            [3, 9, 7, 8, 1, 5, 4, 6, 2],
        ])

    def generate(self, hole_number):
        count = 0
        while count < hole_number:
            y = np.random.randint(0, 8)
            x = np.random.randint(0, 8)
            if self.base_result[y][x] != 0:
                self.base_result[y][x] = 0
                count += 1
        self.logger()
        return self.base_result

    def logger(self):
        log = []
        for x in range(9):
            for y in range(9):
                if self.base_result[y][x] == 0:
                    log.append("△")
                else:
                    log.append(str(self.base_result[y][x]))
                log.append("\t")
            log.append("\n")
        print "".join(log)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number")
    args = parser.parse_args()

    sudoku = SudokuGenerater()
    sudoku.generate(int(args.number))
