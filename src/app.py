#!/usr/bin/env python3

from bots.ibot import IBot
from bots.random.bot import RandomBot
from config import sh

from commands import mandatory

running = False


def setup() -> None:
    global running
    sh.on("test", mandatory.test)
    sh.on("END", mandatory.end)


def run() -> None:
    sh.start()
    while sh.running:
        try:
            sh.getInput()
        except EOFError:
            print("EOF")
            return
        sh.process()


if __name__ == "__main__":
    setup()
    run()
