#!/usr/bin/env python3

class Shell:
    def __init__(self) -> None:
        self.running = False
        self.commands = dict()
        self.currentCmd = None
        self.currentArgs = []

    def start(self) -> None:
        self.running = True

    def on(self, command: str, procedure: callable) -> None:
        self.commands[command] = procedure

    def getInput(self) -> None:
        tmp = input()
        if (not tmp):
            self.clear()
            return
        words = tmp.split()
        self.currentCmd = words[0]
        self.currentArgs = words[1:]

    def dumb(self) -> None:
        print("dumb")
        print(self.currentCmd)
        print(self.currentArgs)

    def process(self) -> None:
        if (not self.currentCmd):
            return
        if self.currentCmd in self.commands:
            self.commands[self.currentCmd]()
        else:
            print("UNKNOWN")

    def clear(self) -> None:
        self.currentCmd = None
        self.currentArgs = []
