PHONY: html-cov

html-cov:
	coverage run --source dish -m pytest
	coverage html
