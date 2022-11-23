#!/usr/bin/env python3

from abc import ABC, abstractmethod


class IBot(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def play(self) -> None:
        pass
