import os
import click


class Interpreter:
	def __init__(self, ctx):
		self.ctx = ctx
	
	
	def feed(self, line):
		# Handle exit command or EOF
		if line in ('', 'exit\n'):
			self.ctx.exit()
		# Blank lines
		elif line.strip() == '':
			return
		
		# Print debug information
		elif line == 'debug\n':
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
			os.system(line)
