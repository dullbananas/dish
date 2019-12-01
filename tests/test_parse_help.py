from dish.parse_help import parse_help


HELP_STR = '''
-a, --long-opt-a

-abcdefg

--long-opt-b
--long-opt-b

  --long-opt-c[=THING]

	-d THING, --long-opt-d
'''


def test_parse_help():
	h = parse_help(HELP_STR)
	assert h.options.sort() == [
		'-a', '-long-opt-a', '--long-opt-b', '--long-opt-c', '-d', '--long-opt-d'
	].sort()
