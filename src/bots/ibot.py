#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Tuple


class IBot(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def opponentMove(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def begin(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def playWith(self, x: int, y: int) -> Tuple[int, int]:
        pass

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def isBoardInitialized(self) -> bool:
        pass

    @abstractmethod
    def initBoard(self, size: int) -> None:
        pass

    @abstractmethod
    def boardIsEmpty(self) -> bool:
        pass
