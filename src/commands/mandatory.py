#!/usr/bin/env python3

from config import sh, brainInfos, brain_settings


def test() -> None:
    sh.dump()
    print(brain_settings)


def end() -> None:
    sh.running = False


def about() -> None:
    keys = list(brainInfos.keys())
    if (not keys):
        return
    for i in range(len(keys) - 1):
        print(keys[i] + "=\"" + str(brainInfos[keys[i]]) + "\"", end=" ")
    print(keys[-1] + "=\"" + str(brainInfos[keys[-1]]) + "\"")


def info() -> None:
    if (len(sh.currentArgs) < 2):
        return
    key = sh.currentArgs[0]
    value = sh.currentArgs[1]
    if (key in brain_settings):
        try:
            brain_settings[key] = int(value)
        except:
            pass
