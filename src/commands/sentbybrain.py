#!/usr/bin/env python3

from config import sh


def error(msg: str) -> None: print("ERROR - " + msg)
def unknown(msg: str) -> None: print("UNKNOWN - " + msg)
def debug(msg: str) -> None: print("DEBUG - " + msg)
def message(msg: str) -> None: print("MESSAGE - " + msg)
def ok() -> None: print("OK")


def move(x: int, y: int) -> None: print(str(x) + "," + str(y))


def on_unknown() -> None:
    unknown(sh.currentCmd if sh.currentCmd else "" + " does not exist")
