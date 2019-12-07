import os
import re
import platform
import time
from click import get_current_context as ctx
from .. import __version__ as __version__


def handle_cwd_tag(attrs):
	return os.getcwd()


def handle_version_tag(attrs):
	return __version__


def handle_platform_tag(attrs):
	return getattr(platform, attrs['name'])()


def handle_git_branch_tag(attrs):
	repo = ctx().obj.current_repo
	(_, ref), _ = repo.refs.follow(b'HEAD')
	match = re.search(r'/([^/]+)$', ref.decode('utf-8'))
	return match[1]


def git_predicate():
	return ctx().obj.current_repo is not None


def handle_time_tag(attrs):
	return time.strftime(attrs['format'])


def register_extension(obj):
	obj.start_tag_handlers['cwd'] = handle_cwd_tag
	obj.start_tag_handlers['version'] = handle_version_tag
	obj.start_tag_handlers['platform'] = handle_platform_tag
	obj.start_tag_handlers['git-branch'] = handle_git_branch_tag
	obj.prompt_predicates['git'] = git_predicate
	obj.start_tag_handlers['time'] = handle_time_tag
