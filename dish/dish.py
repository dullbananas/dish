from . import cli


DEFAULT_CONFIG = {
	'PS1': '$ ',
}


class Dish():
	def __init__(self):
		self.config = DEFAULT_CONFIG
	
	
	def run(self):
		cli.main.main(obj=self)
	
	
	def config_from_dict(self, d):
		self.config = {**self.config, **d}
	
	
	def reset_config(self):
		self.config = DEFAULT_CONFIG
