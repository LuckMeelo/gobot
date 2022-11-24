#!/usr/bin/env python3

class Shell:
    def __init__(self) -> None:
        self.running = False
        self.commands = dict()
        self.currentCmd = None
        self.currentArgs = []
        self.unknown_cmd = lambda: ""

    def on_unknown(self, procedure: callable) -> None:
        self.unknown_cmd = procedure

    def start(self) -> None:
        self.running = True

    def on(self, command: str, procedure: callable) -> None:
        self.commands[command] = procedure

    def getInput(self, case_handle: callable = lambda s: s) -> None:
        tmp = input()
        if (not tmp):
            self.unknown_cmd()
            return
        words = tmp.split()
        self.currentCmd = case_handle(words[0])
        self.currentArgs = words[1:]

    def dump(self) -> None:
        print(self.currentCmd)
        print(self.currentArgs)

    def process(self) -> None:
        if (not self.currentCmd):
            return
        if self.currentCmd in self.commands:
            self.commands[self.currentCmd]()
        else:
            self.unknown_cmd()

    def clear(self) -> None:
        self.currentCmd = None
        self.currentArgs = []
