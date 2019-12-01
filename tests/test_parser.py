from dish import parser


def test_cmd_args():
	assert parser.split_args('arg1 "arg 2"') == ['arg1', 'arg 2']


def test_pipeline(click_ctx):
	with click_ctx:
		args = ['1', '2', '|', '3', '|', '4']
		result = [i for i in parser.split_pipeline(args)]
		assert result == [['1', '2'], ['3'], ['4']]


def test_process_cmd(click_ctx):
	click_ctx.obj.config['ALIASES'] = {
		'uwu': 'owo-owo',
	}
	with click_ctx:
		assert (
			parser.process_cmd(['uwu', 'one', 'two'])
			== ['owo-owo', 'one', 'two']
		)
		assert parser.process_cmd([]) == []
