import GitCommand from GitCommand
import settings
import click

class GitEditSettingsCommand(GitCommand):


    @staticmethod
    def execute(setting: settings, option, value):
        setting.modify(option, value)
        pass