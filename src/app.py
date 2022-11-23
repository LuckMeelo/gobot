#!/usr/bin/env python3

from bots.ibot import IBot
from bots.random.bot import RandomBot
from config import sh, loadBrainInfos

from commands import mandatory
from commands import sentbybrain


def setup() -> None:
    loadBrainInfos()
    sh.on_unknown(sentbybrain.on_unknown)
    sh.on("END", mandatory.end)
    sh.on("ABOUT", mandatory.about)


def run() -> None:
    sh.start()
    while sh.running:
        try:
            sh.getInput(case_handle=lambda s: s.upper())
        except EOFError:
            sentbybrain.error("EOF")
            return
        sh.process()
        sh.clear()


if __name__ == "__main__":
    setup()
    run()
