import GitCommand from GitCommand
import settings
import click

class GitEditSettingsCommand(GitCommand):

    def __init__(self):
        pass

    def execute(self, setting: settings, option, value):
        setting.modify(option, value)
        pass