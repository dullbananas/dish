from dish import ext
import os


def test_handle_color_start_tag():
	assert ext.ansicolor.handle_color_start_tag({
		'fg': 'blue',
		'bg': 'red',
		'style': 'bold faint italic',
	}) == '\033[34;41;1;2;3m'


def test_prompt_goodies():
	assert ext.prompt_goodies.handle_cwd_tag({}) == os.getcwd()
