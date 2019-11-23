import os


class Interpreter:
	def __init__(self, ctx):
		self.ctx = ctx
	
	
	def feed(self, line):
		# Handle exit command or EOF
		if line in ('', 'exit\n'):
			self.ctx.exit()
		else:
			os.system(line)
