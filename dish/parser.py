import shlex
import click


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

	return result


def split_args(line, echo_errors=True):
	try:
		return shlex.split(line)
	except ValueError as e:
		if not echo_errors:
			return []
		click.echo(f'Syntax error: {e}', err=True)


def split_pipeline(args):
	cmd = []
	for arg in args:
		if arg == '|':
			yield process_cmd(cmd)
			cmd = []
		else:
			cmd.append(arg)
	# yield the last part of the pipeline
	yield process_cmd(cmd)
