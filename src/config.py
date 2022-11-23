#!/usr/bin/env python3

from enum import Enum
from shell import Shell
import json

sh = Shell()
brainInfos = dict()


def loadBrainInfos() -> None:
    global brainInfos
    f = open("about.json")
    content = json.load(f)
    for key in content:
        brainInfos[key] = content[key]


class CellValue(Enum):
    DEFAULT = 0
    PLAYED = 0
    OPPONENT = 2


brain_settings = {
    # time limit for each move (milliseconds, 0=play as fast as possible)
    "timeout_turn": 0,
    # time limit of a whole match (milliseconds, 0=no limit)
    "timeout_match": 0,
    # memory limit (bytes, 0=no limit)
    "max_memory": 0,
    # remaining time limit of a whole match (milliseconds)
    "time_left": None,
    # 0=opponent is human, 1=opponent is brain, 2=tournament, 3=network tournament
    "game_type": 0,
    # bitmask or sum of 1=exactly five in a row win, 2=continuous game, 4=renju
    "rule": 1,
    # coordinates X,Y representing current position of the mouse cursor
    "evaluate": (0, 0),
    # folder for persistent files
    "folder": None,
}
