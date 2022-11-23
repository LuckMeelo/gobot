#!/usr/bin/env python3

from config import sh


def error(msg: str) -> None: print("ERROR - " + msg)
def unknown(msg: str) -> None: print("UNKNOWN - " + msg)
def debug(msg: str) -> None: print("DEBUG - " + msg)
def message(msg: str) -> None: print("MESSAGE - " + msg)


def on_unknown() -> None:
    unknown(sh.currentCmd if sh.currentCmd else "" + " does not exist")
