import pytest
import click
from dish import Dish, cli


@pytest.fixture(scope='module')
def click_ctx():
	shell = Dish()
	ctx = click.Context(cli.main, obj=shell)
	return ctx
