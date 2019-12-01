import pytest
import click
from dish import Dish, Interpreter, cli


@pytest.fixture(scope='module')
def click_ctx():
	shell = Dish()
	ctx = click.Context(cli.main, obj=shell)
	return ctx


@pytest.fixture(scope='module')
def interpreter(click_ctx):
	return Interpreter(ctx=click_ctx, verbose=False)
