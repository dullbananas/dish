import re
from collections import namedtuple


Help = namedtuple('Help', 'options')

opt_pattern = re.compile(r'((--[a-zA-Z\-]+)|(-[a-zA-Z])\b)')


def parse_help(helpstr):
	# Contains options, e.g. --help, --verbose, -o
	options = [match[1] for match in opt_pattern.finditer(helpstr)]
	return Help(options=options)
