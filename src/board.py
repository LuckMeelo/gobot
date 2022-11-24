#!/usr/bin/env python3

from config import CellValue


class Board:
    def __init__(self) -> None:
        self.data = None
        self.size = 0

    def build(self, size: int):
        self.data = [[CellValue.DEFAULT * size] * size]
        self.size = size

    def exists(self) -> bool:
        return (self.data)
