import GitCommand from GitCommand
import settings
import click
import subprocess

class GitCheckoutCommand(GitCommand):


    def execute(settings):
        result = subprocess.run("git checkout master", stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, text=True).stdout
        return result