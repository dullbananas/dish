import click
from . import __version__
from .interpreter import Interpreter


@click.command()
@click.version_option(version=__version__, prog_name='Dish shell')
@click.argument('script', type=click.File('r'), default='-')
@click.pass_context # ctx is the Dish object
def main(ctx, script):
	'''Runs SCRIPT as a Dish shell script, or runs an interactive shell if it is
	not specified.
	
	GitHub repository: https://github.com/dullbananas/dish
	'''
	interactive = script.isatty()
	interpreter = Interpreter(ctx)
	
	while True:
		if interactive:
			click.echo('$ ', nl=False)
		interpreter.feed(script.readline())
