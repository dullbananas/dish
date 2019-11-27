import click
import os
from . import __version__
from .interpreter import Interpreter


@click.command()
@click.version_option(version=__version__, prog_name='Dish shell')
@click.argument('script', type=click.File('r'), default='-')
@click.pass_context # ctx.obj is the Dish object
def main(ctx, script):
	'''Runs SCRIPT as a Dish shell script, or runs an interactive shell if it is
	not specified.

	GitHub repository: https://github.com/dullbananas/dish
	'''
	interactive = script.isatty()
	interpreter = Interpreter(ctx)

	if interactive:
		from prompt_toolkit import PromptSession, ANSI, print_formatted_text
		from prompt_toolkit.history import FileHistory

		history_path = os.path.expanduser('~/.dish-history')
		open(history_path, 'a').close()
		psession = PromptSession(
			history=FileHistory(history_path),
			mouse_support=True,
		)

		while True:
			prompt = ANSI(ctx.obj.generate_prompt('PS1'))
			line = psession.prompt(prompt)
			interpreter.feed(line)

	else:
		while True:
			interpreter.feed(script.readline())
