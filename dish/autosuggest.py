from prompt_toolkit.auto_suggest import Suggestion, AutoSuggest
from .parse_help import parse_help
from .parser import split_args, split_pipeline
import subprocess
import glob


class DishSuggest(AutoSuggest):
	def __init__(self, ctx, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helps = {} # Maps command names to parse_help.Help
		self.ctx = ctx # Get the current Click context because this will be running on a different thread


	def get_suggestion(self, buffer, document):
		# Get name of command
		with self.ctx:
			cmds = [i for i in split_pipeline(split_args(document.current_line, echo_errors=False))]
		if len(cmds) == 0:
			return Suggestion(text='')
		if len(cmds[0]) == 0:
			return Suggestion(text='')
		cmdname = cmds[-1][0]

		# Get help
		if len(cmds[-1]) < 2:
			cmdhelp = None
		elif cmdname in self.helps:
			cmdhelp = self.helps[cmdname]
		else:
			try:
				proc = subprocess.run([cmdname, '--help'], capture_output=True)
			except FileNotFoundError:
				return Suggestion(text='')
			cmdhelp = parse_help(proc.stdout.decode('utf-8'))
			self.helps[cmdname] = cmdhelp

		if cmdhelp is None or len(cmdhelp.options) == 0:
			text = ''
		else:
			arg = cmds[-1][-1] # The last arg on the current line
			is_possible_opt = (lambda opt: opt.startswith(arg))
			possible_opts = filter(is_possible_opt, cmdhelp.options)
			text = ''
			for i in possible_opts:
				text = i[len(arg):]
				break

		return Suggestion(text=text)


class FileSuggest(AutoSuggest):

	def __init__(self, ctx, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ctx = ctx

	def get_suggestion(self, buffer, document):
		# Get filename
		with self.ctx:
			cmds = [i for i in split_pipeline(split_args(document.current_line, echo_errors=False))]
		if len(cmds) == 0:
			return Suggestion(text='')
		if len(cmds[-1]) == 0:
			return Suggestion(text='')
		filename = cmds[-1][-1]

		# Get completion
		possible_filenames = glob.glob(filename+'*')
		if len(possible_filenames) == 0:
			return Suggestion(text='')
		else:
			return Suggestion(text=possible_filenames[0][len(filename):])


class CombinedSuggest(AutoSuggest):
	'''Combines multiple AutoSuggest onjects'''

	def __init__(self, objects, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objects = objects

	def get_suggestion(self, buffer, document):
		for obj in self.objects:
			suggestion = obj.get_suggestion(buffer, document)
			if len(suggestion.text) > 0:
				return suggestion
