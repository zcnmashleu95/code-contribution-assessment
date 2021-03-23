from abc import abstractmethod

from Command import Command


class GitCommand(Command):

    @abstractmethod
    def execute(self):
        pass
