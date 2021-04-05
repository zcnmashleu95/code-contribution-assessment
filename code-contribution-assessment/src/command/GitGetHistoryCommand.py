import GitCommand from GitCommand
import settings
import click

class GitGetHistoryCommand(GitCommand):
    def __init__(self):
        pass

    def execute(self, setting: settings):