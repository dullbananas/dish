import click
from . import __version__


@click.command()
@click.version_option(version=__version__, prog_name='Dish shell')
@click.argument('script', type=click.File('r'), default='-')
@click.pass_context # ctx is the Dish object
def main(ctx, script):
	'''Runs SCRIPT as a Dish shell script, or runs an interactive shell if it is
	not specified.
	
	GitHub repository: https://github.com/dullbananas/dish
	'''
	print(f'Script is a tty: {script.isatty()}')
