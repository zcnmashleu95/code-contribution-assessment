import os
import subprocess

from warnings import warn
import command
import request
import settings
import cmd

import click
from click_repl import register_repl

from InputReceiver import InputReceiver
from InputParser import InputParser


# Command to List all files -> git ls-files "*.java"
# Command to Check file -> git blame -p -S <filename>
# Command to Check detail -> git log -p <commit hash>

@click.group()
def capi():
    """A CLI Tool for Code Contribution. \n
    Command 1: Details \n
    Command 2: Details \n
    Command 3: Details \n
    """
    pass


# Test Command
@capi.command()
def hello():
    click.echo("Hello world!")


# Clone Repo Command
@capi.command()
@click.argument('clone-dir', type=click.Path())
def copy(clone_dir):
    out = git_clone(clone_dir)
    if out:
        print("Repository copied to tests folder!")


# def git_clone(url):
#     process = subprocess.Popen(['git', 'clone', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     return namedtuple('Std', 'out, err')(process.stdout.read(), process.stderr.read())
#
# # test on fake url
# out, err = git_clone('http://fake.url')
# print('out = {}\nerr = {}'.format(out, err)


# Clones to Library directly -  need update working DIR
def git_clone(url):
    process = subprocess.Popen(['git', 'clone', url], cwd=r'../tests',
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()  # Wait for process to complete
    if process.stdout.read():
        return False
    return True


@capi.command()
def list_projects():  # Lists Cloned Repos stored
    dirname = r'../tests'
    files = os.listdir(dirname)
    temp = map(lambda name: os.path.join(dirname, name), files)
    print(list(temp))


@capi.command()
@click.argument('file_type')
def list_files(file_type):  # List all files recursively in a repo (e.g. list_files java will list all java files)
    dirname = r'../tests/python-cli'
    type = '*.' + file_type
    process = subprocess.Popen(['git', 'ls-files', type], cwd=dirname)
    process.wait()  # Wait for process to complete

@capi.command()
def analyze_project():  # analyzes selected project
    print("Test Command")


# use command "python main.py repl" to run in interactive mode.
# exit interactive shell with ctrl + D

register_repl(capi)
capi()
