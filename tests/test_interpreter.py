def test_comments(interpreter, capsys):
	captured = capsys.readouterr()
	assert interpreter.feed('# Hello') == False
	assert interpreter.feed('#===') == True
	assert interpreter.feed('this is') == True
	assert interpreter.feed('a multiline') == True
	assert interpreter.feed('comment==#') == False
	assert captured.out == ''
	assert captured.err == ''
