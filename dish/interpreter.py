import os
import click
from . import procs


class Interpreter:
	def __init__(self, ctx, verbose):
		self.ctx = ctx
		self.verbose = verbose


	def feed(self, line):
		# Handle exit command or EOF
		if line == 'exit':
			self.ctx.exit()
		# Blank lines
		elif line.strip() == '':
			return

		# Print debug information
		elif line == 'debug':
			click.echo('Configuration values:')
			for key, val in self.ctx.obj.config.items():
				click.echo(f'  {key} = {repr(val)}')
		# cd
		elif line.startswith('cd '):
			dirname = line[3:].strip()
			os.chdir(os.path.expanduser(dirname))

		# Comments
		elif line.strip()[0] == '#':
			return
		else:
			procs.run_line(line, echo_args=self.verbose)
