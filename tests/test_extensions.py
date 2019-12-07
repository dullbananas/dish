from dish import ext, __version__ as dish_version
import os
import platform
import time


def test_handle_color_start_tag():
	assert ext.ansicolor.handle_color_start_tag({
		'fg': 'blue',
		'bg': 'red',
		'style': 'bold faint italic',
	}) == '\033[34;41;1;2;3m'


def test_prompt_goodies():
	assert ext.prompt_goodies.handle_cwd_tag({}) == os.getcwd()
	assert ext.prompt_goodies.handle_version_tag({}) == dish_version
	assert ext.prompt_goodies.handle_platform_tag({
		'name': 'node',
	}) == platform.node()
	assert ext.prompt_goodies.handle_time_tag({'format': '%I'}) == time.strftime('%I')
