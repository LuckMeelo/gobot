#!/usr/bin/env python3

from bots.ibot import IBot
from board import Board, CellValue
from typing import Tuple


class RandomBot(IBot):
    def __init__(self) -> None:
        self.board = Board()
        super().__init__()

    def begin(self) -> Tuple[int, int]:
        x, y = 0, 0
        self.board.data[y][x] = CellValue.PLAYED
        return (x, y)

    def play(self) -> Tuple[int, int]:
        pass

    def isBoardInitialized(self) -> bool:
        return (self.board.created())

    def initBoard(self, size: int) -> None:
        self.board.build(size)

    def boardIsEmpty(self) -> bool:
        return self.board.isEmpty()
