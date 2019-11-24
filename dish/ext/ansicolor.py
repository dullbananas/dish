from colors.colors import _color_code as get_color_num


def handle_color_start_tag(attrs):
	# This list will contain the numbers that will be in the returned value. For
	# example, if this is [30, 31], then the re
	nums = []
	if 'fg' in attrs:
		nums.append(get_color_num(attrs['fg'], 30))
	if 'bg' in attrs:
		nums.append(get_color_num(attrs['bg'], 40))
	joined_nums = ';'.join([str(i) for i in nums])
	return f'\033[{joined_nums}m'
