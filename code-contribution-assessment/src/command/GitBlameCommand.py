import GitCommand from GitCommand
import settings
import click

class GitBlameCommand(GitCommand):
    def __init__(self):
        pass

    def execute(self, setting: settings):
        filepath = setting.getSetting()
        pass