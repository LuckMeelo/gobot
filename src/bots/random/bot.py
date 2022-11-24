#!/usr/bin/env python3

from bots.ibot import IBot
from board import Board, CellValue
from typing import Tuple
import random


class RandomBot(IBot):
    def __init__(self) -> None:
        self.board = Board()
        self.playables = []
        super().__init__()

    def opponentMove(self, x: int, y: int) -> None:
        if (x >= self.board.size or y >= self.board.size):
            raise Exception("invalid position")
        self.board.data[y][x] = CellValue.OPPONENT
        try:
            id = self.playables.index((x, y))
            self.playables.pop(id)
        except ValueError:
            raise Exception("cell is not Empty")

    def begin(self) -> Tuple[int, int]:
        return self.play()

    def play(self, x: int, y: int) -> Tuple[int, int]:
        if (x >= self.board.size or y >= self.board.size):
            raise Exception("invalid position")
        self.board.data[y][x] = CellValue.PLAYED
        try:
            id = self.playables.index((x, y))
            self.playables.pop(id)
        except ValueError:
            raise Exception("cell is not Empty")

    def play(self) -> Tuple[int, int]:
        id = random.randint(0, len(self.playables) - 1)
        x, y = self.playables[id]
        self.playables.pop(id)
        self.board.data[y][x] = CellValue.PLAYED
        return (x, y)

    def isBoardInitialized(self) -> bool:
        return (self.board.created())

    def initBoard(self, size: int) -> None:
        self.board.build(size)
        for i in range(len(self.board.data)):
            for j in range(len(self.board.data[i])):
                self.playables.append((j, i))

    def boardIsEmpty(self) -> bool:
        return self.board.isEmpty()
