import os
import re
from click import get_current_context as ctx


def handle_cwd_tag(attrs):
	return os.getcwd()


def handle_git_branch_tag(attrs):
	repo = ctx().obj.current_repo
	(_, ref), _ = repo.refs.follow(b'HEAD')
	match = re.search(r'/([^/]+)$', ref.decode('utf-8'))
	return match[1]


def git_predicate():
	return ctx().obj.current_repo is not None


def register_extension(obj):
	obj.start_tag_handlers['cwd'] = handle_cwd_tag
	obj.start_tag_handlers['git-branch'] = handle_git_branch_tag
	obj.prompt_predicates['git'] = git_predicate
