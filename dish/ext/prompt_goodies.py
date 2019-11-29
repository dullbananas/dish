import os


def handle_cwd_tag(attrs):
	return os.getcwd()


def register_extension(obj):
	obj.start_tag_handlers['cwd'] = handle_cwd_tag
