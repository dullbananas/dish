import shlex
import click
import os


def process_cmd(args, called_self=False):
	if len(args) == 0:
		return args

	result = args

	# Replace aliases
	if not called_self:
		aliases = click.get_current_context().obj.config['ALIASES']
		if result[0] in aliases:
			substitution = process_cmd(split_args(aliases[result[0]]), True)
			if len(result) == 1:
				result = substitution
			else:
				result = substitution + result[1:]

	# Expand ~ (user dir)
	for i, arg in enumerate(result):
		if arg.startswith('~'):
			result[i] = os.path.expanduser(arg)

	return result


def split_args(line, echo_errors=True):
	try:
		return shlex.split(line)
	except ValueError as e:
		if not echo_errors:
			return []
		click.echo(f'Syntax error: {e}', err=True)


def split_pipeline(args):
	# to prevent errors
	if len(args) == 0:
		return []
	if args[0] == '|':
		del args[0]
	if args[-1] == '|':
		del args[-1]

	cmd = []
	for arg in args:
		if arg == '|':
			yield process_cmd(cmd)
			cmd = []
		else:
			cmd.append(arg)
	# yield the last part of the pipeline
	yield process_cmd(cmd)
