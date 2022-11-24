#!/usr/bin/env python3
from enum import Enum


class CellValue(Enum):
    DEFAULT = 0
    PLAYED = 1
    OPPONENT = 2


class Board:
    def __init__(self) -> None:
        self.data = None
        self.size = 0

    def build(self, size: int) -> None:
        self.data = [[CellValue.DEFAULT] * size] * size
        self.size = size

    def created(self) -> bool:
        return (self.data)

    def isEmpty(self) -> bool:
        if not (self.data):
            return True
        for i in self.data:
            for j in i:
                if j != CellValue.DEFAULT:
                    return False
        return True
