import cmd, sys


class Run(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    def running(self):
        subprocess.Popen(
            ['git', 'status'])
