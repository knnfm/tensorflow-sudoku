#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np

from sudoku_generater import SudokuGenerater

class CatchBall:
    def __init__(self):
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        self.enable_actions = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    # 現状の取得
    def observe(self):
        return self.sudoku, self.reward, self.terminal

    # アクション実行
    def execute_action(self, action):
        self.reward = 0
        self.terminal = False


        print "------------"
        self.sudoku_generater.logger(self.sudoku)
        for x in range(9):
            for y in range(9):
                if (int(self.sudoku[y][x]) == 0):
                    self.sudoku[y][x] = action
        self.sudoku_generater.logger(self.sudoku)

        is_end = True
        for x in range(9):
            for y in range(9):
                if (int(self.sudoku[y][x]) == 0):
                    is_end = False


        if is_end == True:
            self.terminal = True
            if self.is_success() == True:
                print "Reward 1"
                self.reward = 1
            else:
                print "Reward -1"
                self.reward = -1

    # 数独が正解か
    def is_success(self):
        result = True
        # Check col
        for x in range(9):
            count = 0
            for y in range(9):
                count += int(self.sudoku[y][x])

            if count == 45:
                continue
            else:
                return False

        # Check row
        for y in range(9):
            count = 0
            for x in range(9):
                count += int(self.sudoku[y][x])

            if count == 45:
                continue
            else:
                return False

        return True

    # 新規問題生成
    def set_question(self):
        self.sudoku_generater = SudokuGenerater()
        self.sudoku = self.sudoku_generater.generate(1)

    def reset(self):
        self.reward = 0
        self.terminal = False
