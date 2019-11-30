from colors.colors import _color_code as get_color_num, STYLES


def handle_color_start_tag(attrs):
	# This list will contain the numbers that will be in the returned value. For
	# example, if this is [30, 31], then the returned value is '\033[30;31m'
	nums = []
	if 'fg' in attrs:
		nums.append(get_color_num(attrs['fg'], 30))
	if 'bg' in attrs:
		nums.append(get_color_num(attrs['bg'], 40))
	if 'style' in attrs:
		for style_name in attrs['style'].split(' '):
			nums.append(STYLES.index(style_name))
	joined_nums = ';'.join([str(i) for i in nums])
	return f'\033[{joined_nums}m'


def handle_color_end_tag():
	return '\033[0;39;49m'


def register_extension(obj):
	obj.start_tag_handlers['color'] = handle_color_start_tag
	obj.end_tag_handlers['color'] = handle_color_end_tag
