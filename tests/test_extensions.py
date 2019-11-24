from dish.ext.ansicolor import handle_color_start_tag


def test_handle_color_start_tag():
	assert handle_color_start_tag({
		'fg': 'blue',
		'bg': 'red',
	}) == '\033[34;41m'
