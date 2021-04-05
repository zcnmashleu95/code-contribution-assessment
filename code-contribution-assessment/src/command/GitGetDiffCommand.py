import GitCommand from GitCommand
import settings
import click

class GitGetDiffCommand(GitCommand):
    def __init__(self):
        pass

    def execute(self, setting: settings, option, value):
