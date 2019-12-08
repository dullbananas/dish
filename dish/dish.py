from . import cli
from dulwich.repo import Repo
from dulwich.errors import NotGitRepository
from xml.parsers.expat import ParserCreate
import os


DEFAULT_CONFIG = {
	'PS1': '$ ',
	'PS2': '> ',
	'ALIASES': {},
}


class Dish():
	'''This is the main class. It holds configuration, extensions, and more. It
	works a bit similar to Flask's ``Flask`` class.

	:property current_repo: Holds the current Git repository, or ``None`` if you
	                        are not in a repository.
	'''

	#: This is a dictionary of functions used to handle start tags in prompts.
	#: These functions accept one argument, which is a dictionary containing the
	#: XML tag's attributes. The function must return a string to replace the tag
	#: with.
	#:
	#: For example, when the prompt parser encounters ``<thing value="8">``, it
	#: will call ``self.start_tag_handlers['thing']({'value': '8'})``.
	start_tag_handlers = {}

	#: This is just like ``start_tag_handlers``, but it's for end tags, and the
	#: functions in it accept no arguments. If you want to create a self-closing
	#: tag, such as ``<cwd/>``, then you only need to add a function to
	#: ``start_tag_handlers``.
	end_tag_handlers = {}

	#: This is a dictionary of functions that accept no arguments and return a
	#: boolean value. These functions are used for ``<if_...>`` tags.
	prompt_predicates = {}

	#: This holds the amount of seconds it took to run the previous command. The
	#: initial value is 0.
	previous_cmd_duration = 0

	def __init__(self):
		self.config = DEFAULT_CONFIG

		self.start_tag_handlers = {}
		self.end_tag_handlers = {}
		self.prompt_predicates = {}

		self.previous_cmd_duration = 0


	def run(self):
		'''This method runs the shell. In your shell configuration script, this
		should be protected using an ``if __name__ == '__main__'`` condition.
		'''
		cli.main.main(obj=self)


	def config_from_dict(self, d):
		'''This method adds the configuration values in a dictionary to the
		current configuration.

		:param d: A dictionary with configuration values.
		'''
		self.config = {**self.config, **d}


	def reset_config(self):
		'''This resets the configuration to the default values.
		'''
		self.config = DEFAULT_CONFIG


	def register_extension(self, module, **kwargs):
		'''This initializes an extension module.

		:param module: A module with a ``register_extension`` function.
		:param kwargs: Additional arguments to pass to the ``register_extension``
		               function of the module.
		'''
		module.register_extension(self, **kwargs)


	def _handle_start_tag(self, name, attrs):
		if self._skip_this_data:
			return
		if name in self.start_tag_handlers:
			self._prompt_result += str(self.start_tag_handlers[name](attrs))
		elif name.startswith('if_'):
			if not self.prompt_predicates[name[3:]]():
				self._skip_this_data = True


	def _handle_end_tag(self, name):
		if name.startswith('if_'):
			self._skip_this_data = False
		elif self._skip_this_data:
			return
		elif name in self.end_tag_handlers:
			self._prompt_result += str(self.end_tag_handlers[name]())


	def _handle_text(self, data):
		if not self._skip_this_data:
			self._prompt_result += data


	def generate_prompt(self, prompt_type):
		'''Generates the prompt string.

		:param prompt_type: Can be either ``PS1`` or ``PS2``.
		'''
		self._prompt_result = ''
		self._skip_this_data = False # This is set to True by <if_...> tags if the condition is False, and tells _handle_text to ignore the stuff
		parser = ParserCreate()
		parser.StartElementHandler = self._handle_start_tag
		parser.EndElementHandler = self._handle_end_tag
		parser.CharacterDataHandler = self._handle_text
		parser.Parse(f'<prompt>{self.config[prompt_type]}</prompt>', True)
		return self._prompt_result


	def _get_current_repo(self, path=None):
		if path == None:
			path = os.getcwd()
		try:
			return Repo(path)
		except NotGitRepository:
			if path == '/':
				return None
			else:
				return self._get_current_repo(path=os.path.dirname(path))


	@property
	def current_repo(self):
		return self._get_current_repo()
