from abc import abstractmethod

from Command import Command


class GitCommand(Command):

    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass
