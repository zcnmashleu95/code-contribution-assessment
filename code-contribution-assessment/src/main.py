import subprocess
from collections import namedtuple
import sys
import os
from warnings import warn

import click


@click.group()
def capi():
    """A CLI Tool for Code Contribution.

    Command 1: Details \n
    Command 2: Details \n
    Command 3: Details \n

    """
    pass


# def git_clone(url):
#     process = subprocess.Popen(['git', 'clone', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     return namedtuple('Std', 'out, err')(process.stdout.read(), process.stderr.read())
#
# # test on fake url
# out, err = git_clone('http://fake.url')
# print('out = {}\nerr = {}'.format(out, err)
# Commands to be refactored into respective modules
@capi.command()
@click.argument('clone-dir', type=click.Path())
def copy(clone_dir):
    print("This is the Copy Command")
    out = git_clone(clone_dir)
    print(out)  # Bool Test if Successfully Copy


# Clones to Library directly -  need update working DIR
def git_clone(url):
    process = subprocess.Popen(['git', 'clone', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if not process.stdout.read():
        warn(process.stderr.read())
        return False

    return True


@capi.command()
def logs(settings):
    print("This is the Git Logs Command")
    logpro()


# Need to optimize processes / git commands has to be run from the folder we are checking
def logpro(settings):
    lines = subprocess.Popen(
        ['git', 'log'])
    print(lines)


@capi.command()
def analyze():
    print("This is the analyze Command")


@capi.command()
def diff():
    lines = subprocess.Popen(
        ['git', 'diff'])


# to be refactored into git edit settings command
@capi.command()
@capi.argument('option_number', type=int)
@capi.argument('new_setting')
def set_setting(settings):
    settings.modify(option_number, new_setting)


# to be refactored into input parser
@capi.command()
def get_input():
    new_request = click.prompt("Enter your Request:")


if __name__ == "__main__":
    capi(prog_name='capi')
