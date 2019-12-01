import os
import click
from . import procs


class Interpreter:
	def __init__(self, ctx, verbose):
		self.ctx = ctx
		self.verbose = verbose
		self.lines = []


	def feed(self, line):
		if len(self.lines) > 0:
			# Multi-line comments
			if self.lines[0].startswith('#==') and line.endswith('==#'):
				self.lines = []
				return False

			return True

		# Handle exit command or EOF
		if line == 'exit':
			self.ctx.exit()
		# Blank lines
		elif line.strip() == '':
			pass

		# Print debug information
		elif line == 'debug':
			click.echo('Configuration values:')
			for key, val in self.ctx.obj.config.items():
				click.echo(f'  {key} = {repr(val)}')
		# cd
		elif line.startswith('cd '):
			try:
				dirname = line[3:].strip()
				os.chdir(os.path.expanduser(dirname))
			except OSError as e:
				click.echo(e, err=True)

		# Start of multiline comments
		elif line.startswith('#=='):
			self.lines.append(line)
			return True

		# Single-line comments
		elif line.strip()[0] == '#':
			pass

		# Normal commands
		else:
			try:
				with self.ctx:
					procs.run_line(line, echo_args=self.verbose)
			except FileNotFoundError as e:
				click.echo(f'Command not found: {e.filename}', err=True)

		self.lines = []
		return False
