import GitCommand from GitCommand
import settings
import click

class GitEditSettingsCommand(GitCommand):
    def execute(self, settings, option, value):
        settings.modify(option_number, new_setting)
        pass