CONTENT = '''
uwu 0
uwu 1
uwu 2
owo 0
owo 1
owo 2
owo-owo0
owo-owo1
owo-owo2
'''

GREP_RESULT = '''
owo 0
owo-owo0
'''


def test_pipelines(interpreter, capfd, tmp_path):
	assert interpreter.feed(f'cd {tmp_path}') == False
	f = tmp_path / 'file.txt'
	f.write_text(CONTENT)
	assert interpreter.feed(f'cat {f} | grep "0" | grep "owo"') == False
	captured = capfd.readouterr()
	assert captured.out.strip() == GREP_RESULT.strip()
