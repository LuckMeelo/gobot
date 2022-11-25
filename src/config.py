#!/usr/bin/env python3

from shell import Shell
from bots.abot import ABot

sh = Shell()

brainInfos = {
    "name": "goBot",
    "version": 1.0,
    "author": "LuckMeelo",
    "country": "BJ"
}

MINIMUM_BOARD_SIZE = 5

# change Bot here
bot = ABot()

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
}
