import os
import time


def test_comments(interpreter, capfd):
	assert interpreter.feed('# Hello') == False
	captured = capfd.readouterr()
	assert captured.out == ''
	assert captured.err == ''

	assert interpreter.feed('#===') == True
	assert interpreter.feed('this is') == True
	assert interpreter.feed('a multiline') == True
	assert interpreter.feed('comment==#') == False
	captured = capfd.readouterr()
	assert captured.out == ''
	assert captured.err == ''


def test_commands(interpreter, capfd):
	assert interpreter.feed('echo "Hello world"') == False
	captured = capfd.readouterr()
	assert captured.out.strip() == 'Hello world'
	assert captured.err == ''

	assert interpreter.feed('cd /') == False
	captured = capfd.readouterr()
	assert captured.out.strip() == ''
	assert captured.err == ''
	assert os.getcwd() == '/'


def test_errors(interpreter, capfd):
	assert interpreter.feed('uwu "hello moron"') == False
	captured = capfd.readouterr()
	assert captured.out == ''
	assert 'not found' in captured.err
