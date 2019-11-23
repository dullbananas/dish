import click
from . import cli


class Dish():
	def run(self):
		cli.main.main(obj=self)
