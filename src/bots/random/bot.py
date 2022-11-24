#!/usr/bin/env python3

from bots.ibot import IBot
from board import Board


class RandomBot(IBot):
    def __init__(self) -> None:
        self.board = Board()
        super().__init__()

    def play(self) -> None:
        pass

    def isBoardInitialized(self) -> bool:
        return (self.board.created())

    def initBoard(self, size: int) -> None:
        self.board.build(size)
