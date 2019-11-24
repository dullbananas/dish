from dish import ext


def test_handle_color_start_tag():
	assert ext.ansicolor.handle_color_start_tag({
		'fg': 'blue',
		'bg': 'red',
	}) == '\033[34;41m'
