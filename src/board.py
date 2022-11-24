#!/usr/bin/env python3
from enum import Enum


class CellValue(Enum):
    DEFAULT = 0
    PLAYED = 0
    OPPONENT = 2


class Board:
    def __init__(self) -> None:
        self.data = None
        self.size = 0

    def build(self, size: int):
        self.data = [[CellValue.DEFAULT for i in range(size)] * size]
        self.size = size

    def created(self) -> bool:
        return (self.data)
