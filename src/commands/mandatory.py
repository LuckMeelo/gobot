#!/usr/bin/env python3

from config import sh, brainInfos, brain_settings, bot, MINIMUM_BOARD_SIZE
from commands import sentbybrain
from shell import Shell


def test() -> None:
    sh.dump()
    print(brain_settings)


def board() -> None:
    if not bot.isBoardInitialized():
        sentbybrain.error("board is not initialized")
        return
    gameAlreadyStarted = (not bot.boardIsEmpty())
    sh.getInput()
    while sh.currentCmd != "DONE":
        try:
            tmp = [int(i) for i in sh.currentCmd.split(',')]
            if (len(tmp) != 3):
                continue
            try:
                if (tmp[2] in [1, 2]) and gameAlreadyStarted:
                    sentbybrain.error("game already started")
                    return
                if (tmp[2] == 1):
                    bot.playWith(tmp[0], tmp[1])
                if (tmp[2] == 2):
                    bot.opponentMove(tmp[0], tmp[1])
            except Exception as e:
                sentbybrain.error(str(e))
                return
        except:
            pass
        sh.clear()
        sh.getInput()
    botx, boty = bot.play()
    sentbybrain.move(botx, boty)


def turn() -> None:
    if not bot.isBoardInitialized():
        sentbybrain.error("board is not initialized")
        return
    if (len(sh.currentArgs) < 1):
        sentbybrain.error("invalid parameter")
        return
    a, b = "", ""
    if (len(sh.currentArgs) == 1):
        if (',' in sh.currentArgs[0]):
            tmp = sh.currentArgs[0].split(',')
            a, b = tmp[0], tmp[1]
        else:
            sentbybrain.error("invalid parameter")
            return
    else:
        a, b = sh.currentArgs[0], sh.currentArgs[1]
    try:
        x, y = int(a), int(b)
        try:
            bot.opponentMove(x, y)
        except Exception as e:
            sentbybrain.error(str(e))
            return
    except:
        sentbybrain.error("invalid parameter")
        return
    botx, boty = bot.play()
    sentbybrain.move(botx, boty)


def begin() -> None:
    if not bot.isBoardInitialized():
        sentbybrain.error("board is not initialized")
        return
    if not (bot.boardIsEmpty()):
        sentbybrain.error("game already started")
        return
    x, y = bot.begin()
    sentbybrain.move(x, y)


def start() -> None:
    if (len(sh.currentArgs) < 1):
        sentbybrain.error("parameter cant be empty")
        return
    if bot.isBoardInitialized():
        sentbybrain.error("board is already initialized")
        return
    invalid = False
    try:
        size = int(sh.currentArgs[0])
        invalid = (size < MINIMUM_BOARD_SIZE)
    except:
        invalid = True
    if (invalid):
        sentbybrain.error("invalid size")
    else:
        bot.initBoard(size)
        sentbybrain.ok()


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
