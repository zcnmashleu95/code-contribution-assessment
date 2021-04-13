import os
import subprocess

import click
from click_repl import register_repl
from pathlib import Path
import re

# Command to List all files -> git ls-files "*.java"
# Command to Check file -> git blame -p -S <filename>
# Command to Check detail -> git log -p <commit hash>

# Directory Path Settings
project_dir = r'../analyze'


@click.group()
def capi():
    """A CLI Tool for Code Contribution. \n
    """
    pass


# Clone Repo Command
@capi.command()
@click.argument('clone-dir', type=click.Path())
def copy(clone_dir):
    """This Script is a copy of the 'Git Clone' Command"""
    git_clone(clone_dir)


# Helper Function
# TODO: Add Error Handling
# Captures the output of Git Clone command in stdout / stderr.
def git_clone(url):
    process = subprocess.Popen(['git', 'clone', url], cwd=project_dir,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()  # Wait for process to complete


@capi.command()
@click.argument('project', )
@click.argument('file_type')
def list_files(project, file_type):
    """Listing of Files in a Project"""
    working_dir = os.path.join(project_dir, project)
    working_filetype = '*.' + file_type
    process = subprocess.Popen(['git', 'ls-files', working_filetype], cwd=working_dir)
    process.wait()  # Wait for process to complete


@capi.command()
def list_projects():
    """List Cloned Repositories Stored"""
    dirname = project_dir
    files = os.listdir(dirname)
    temp = map(lambda name: os.path.join(name), files)
    print(*list(temp), sep="\n")


@capi.command()
@click.argument('project')
@click.argument('file_path')
def analyze_file(project, file_path):
    """Analyze Selected Project File"""
    working_dir = os.path.join(project_dir, project)
    make_dir(working_dir)
    list = get_blame_details(working_dir, file_path)
    get_log_details(working_dir, list, file_path)


# Helper Function
# Creates Nested path in selected project if does not exist
def make_dir(loc):
    Path(os.path.join(loc, "results")).mkdir(parents=True, exist_ok=True)


# Helper Function
# Executes git blame and stores location results/blame_results
# analyze-file python-cli py-test/pytest/__main__.py
def get_blame_details(curr_dir, file_path):
    working_dir = curr_dir + "/results"
    f = open(os.path.join(working_dir, "blame_result.txt"), "w")
    process = subprocess.Popen(['git', 'blame', '-P', file_path], cwd=curr_dir
                               , stdout=f, stderr=subprocess.PIPE)
    process.wait()  # Wait for process to complete
    return list(parse_blame(working_dir, "/blame_result.txt"))


# Helper Function
# Parses blame_result (exmaple)
# e2d275a0 (Yralle Lesly 2021-01-25 20:16:29 +0800  1) import sys
# e2d275a0 (Yralle Lesly 2021-01-25 20:16:29 +0800  2) from .classmodule import MyClass
# The above Becomes -> List of Tuples (No of items in the list == Number of Lines in that File)
# [(e2d275a0, Yralle Lesly 2021-01-25 20:16:29 +0800  1), (e2d275a0, Yralle Lesly 2021-01-25 20:16:29 +0800  1)]
def parse_blame(path, file_name):
    file = open(path + file_name, "r")
    lines = file.readlines()

    sha_list = []
    author_list = []
    for line in lines:
        sha_list.append(line[0:8])
        author_list.append(re.search(r'(\((?:\[??[^\[]*?\)))', line).group(1))

    return zip(sha_list, author_list)


# Helper Function
# Executes Git Log -p <commit-hash>
def get_log_details(curr_dir, blame_list, file_path):
    # print(*blame_list, sep="\n")
    # print(len(blame_list))

    # test code

    test = ""
    for ln in blame_list:
        test = ln[0]

    get_git_log(test, curr_dir)
    parse_log(file_path)


def get_git_log(sha, curr_dir):
    working_dir = curr_dir + "/results"
    f = open(os.path.join(working_dir, "log_results.txt"), "w")
    process = subprocess.Popen(['git', 'show', '-P', sha], cwd=curr_dir
                               , stdout=f, stderr=subprocess.PIPE)
    process.wait()  # Wait for process to complete


def parse_log(file_path):
    print(file_path)


register_repl(capi)
capi()
