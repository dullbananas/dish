#!/usr/bin/env python3

from setuptools import setup
import re

with open('README.md', 'r') as f:
	readme = f.read()

def getprop(prop):
	match = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open('dish/__init__.py').read())
	return match.group(1)


setup(
	name='dish',
	version=getprop('__version__'),
	description='A new, modern Unix shell implemented in pure Python with Flask-like configuration and extensibility',
	long_description=readme,
	long_description_content_type='text/markdown',

	author='Dull Bananas',
	author_email='dull.bananas0@gmail.com',
	url='https://github.com/dullbananas/dish',

	license='MIT',

	packages=['dish'],
	install_requires=[
		'click',
		'ansicolors',
		'prompt_toolkit',
	],
	python_requires='>=3.7',

	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: Unix',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: System :: Shells',
		'Topic :: Utilities',
	],
)
