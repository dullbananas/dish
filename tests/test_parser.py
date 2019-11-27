from dish import parser


def test_cmd_args():
	assert parser.split_args('arg1 "arg 2"') == ['arg1', 'arg 2']


def test_pipeline():
	args = ['1', '2', '|', '3', '|', '4']
	result = [i for i in parser.split_pipeline(args)]
	assert result == [['1', '2'], ['3'], ['4']]
