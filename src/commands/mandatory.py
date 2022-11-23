#!/usr/bin/env python3

from config import sh, brainInfos


def test() -> None:
    sh.dump()


def end() -> None:
    sh.running = False


def about() -> None:
    keys = list(brainInfos.keys())
    if (not keys):
        return
    for i in range(len(keys) - 1):
        print(keys[i] + "=\"" + str(brainInfos[keys[i]]) + "\"", end=" ")
    print(keys[-1] + "=\"" + str(brainInfos[keys[-1]]) + "\"")
