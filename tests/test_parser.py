from dish import parser


def cumulative_iter(stuff):
	# Example: when this is called with [0, 1, 2, 3], it yields these:
	# []
	# [0]
	# [0, 1]
	# [0, 1, 2]
	# [0, 1, 2, 3]
	# This is used to make sure that Dish's auto completion doesn't produce an
	# error when the user is in the middle of typing a command, and it is
	# temporarily invalid.
	for i in range(len(stuff) + 1):
		yield stuff[0:i]


def test_cumulative_iter():
	l = [0, 1, 2, 3]
	result = [i for i in cumulative_iter(l)]
	assert result == [
		[],
		[0],
		[0, 1],
		[0, 1, 2],
		[0, 1, 2, 3],
	]


def test_cmd_args():
	for i in cumulative_iter('arg1 "arg 2"'):
		args = parser.split_args(i)
	assert args == ['arg1', 'arg 2']


def test_pipeline(click_ctx):
	with click_ctx:
		args = ['1', '2', '|', '3', '|', '4']
		for i in cumulative_iter(args):
			result = [j for j in parser.split_pipeline(i)]
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
