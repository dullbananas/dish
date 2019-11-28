import shlex
import click


def split_args(line):
	try:
		return shlex.split(line)
	except ValueError as e:
		click.echo(f'Syntax error: {e}', err=True)


def split_pipeline(args):
	cmd = []
	for arg in args:
		if arg == '|':
			yield cmd
			cmd = []
		else:
			cmd.append(arg)
	# yield the last part of the pipeline
	yield cmd
