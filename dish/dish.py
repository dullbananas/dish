from . import cli
from xml.parsers.expat import ParserCreate


DEFAULT_CONFIG = {
	'PS1': '$ ',
}


class Dish():
	def __init__(self):
		self.config = DEFAULT_CONFIG
		self.start_tag_handlers = {}
		self.end_tag_handlers = {}
	
	
	def run(self):
		cli.main.main(obj=self)
	
	
	def config_from_dict(self, d):
		self.config = {**self.config, **d}
	
	
	def reset_config(self):
		self.config = DEFAULT_CONFIG
	
	
	def register_extension(self, module, **kwargs):
		module.register_extension(self, **kwargs)
	
	
	def _handle_start_tag(self, name, attrs):
		if name in self.start_tag_handlers:
			self._prompt_result += self.start_tag_handlers[name](attrs)
	
	
	def _handle_end_tag(self, name):
		if name in self.end_tag_handlers:
			self._prompt_result += self.end_tag_handlers[name]()
	
	
	def _handle_text(self, data):
		self._prompt_result += data
	
	
	def generate_prompt(self, prompt_type):
		self._prompt_result = ''
		parser = ParserCreate()
		parser.StartElementHandler = self._handle_start_tag
		parser.EndElementHandler = self._handle_end_tag
		parser.CharacterDataHandler = self._handle_text
		parser.Parse(f'<prompt>{self.config[prompt_type]}</prompt>', True)
		return self._prompt_result
