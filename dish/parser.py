import shlex


def split_args(line):
	return shlex.split(line)


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
