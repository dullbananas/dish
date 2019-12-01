import click
import os
from . import __version__
from .interpreter import Interpreter


@click.command()
@click.version_option(version=__version__, prog_name='Dish shell')
@click.option('-v/ ', '--verbose/--no-verbose', default=False,
help='Shows parsed command line arguments before running them')
@click.argument('script', type=click.File('r'), default='-')
@click.pass_context # ctx.obj is the Dish object
def main(ctx, verbose, script):
	'''Runs SCRIPT as a Dish shell script, or runs an interactive shell if it is
	not specified.

	GitHub repository: https://github.com/dullbananas/dish
	'''
	interactive = script.isatty()
	interpreter = Interpreter(
		ctx=ctx,
		verbose=verbose,
	)

	if interactive:
		from prompt_toolkit import PromptSession, ANSI
		from prompt_toolkit.history import FileHistory
		from prompt_toolkit.lexers import PygmentsLexer
		from prompt_toolkit.auto_suggest import ThreadedAutoSuggest
		from .autosuggest import DishSuggest
		from pygments.lexers.shell import BashLexer

		history_path = os.path.expanduser('~/.dish-history')
		open(history_path, 'a').close()
		psession = PromptSession(
			auto_suggest=ThreadedAutoSuggest(DishSuggest(ctx=ctx)),
			history=FileHistory(history_path),
			lexer=PygmentsLexer(BashLexer),
			mouse_support=True,
		)

		gprompt = ctx.obj.generate_prompt

		while True:
			prompt1 = ANSI(gprompt('PS1'))
			prompt2 = ANSI(gprompt('PS2'))
			line = psession.prompt(prompt1)
			needs_more = interpreter.feed(line)
			while needs_more:
				line = psession.prompt(prompt2)
				needs_more = interpreter.feed(line)

	else:
		while True:
			line = script.readline()
			if line == '':
				break
			else:
				interpreter.feed(line[:-1])
