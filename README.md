<h1 align="center">
  <img src="artwork/dish-logo.png" height="128" align="center" />
</h1>

<h4 align="center">A new Unix shell implemented in Python</h4>

***
[![Gitter](https://img.shields.io/gitter/room/dullbananas/dish)](https://gitter.im/dish-shell/community)
![Codacy coverage](https://img.shields.io/codacy/coverage/1faac136e1a5459b9141fa6cc03cf0bd)
![Codacy grade](https://img.shields.io/codacy/grade/1faac136e1a5459b9141fa6cc03cf0bd)
![Maintenance](https://img.shields.io/maintenance/yes/2019)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dish)
![PyPI](https://img.shields.io/pypi/v/dish)
![PyPI - License](https://img.shields.io/pypi/l/dish)
***

Dish is a new Unix shell implemented in Python with Flask-like configuration and extensibility. It is currently in alpha stage of development. It works by having a Python script called "dish" somewhere in `PATH`. This script looks a bit like a single-file Flask application. Here is an example:

```python3
#!/usr/bin/env python3

from dish import Dish
dish = Dish()

# ansicolor color to be used in PS1 prompt
from dish.ext import ansicolor
dish.register_extension(ansicolor)

dish.config['PS1'] = '<color fg="pink">$</color> '

if __name__ == '__main__':
    dish.run()
```

## Installation

To install the latest stable version:

```console
$ pip3 install --user dish
```

To install the master branch:

```console
$ git clone https://github.com/dullbananas/dish.git
$ cd dish
$ python3 setup.py install --user
```

## Project Links

* [Documentation](https://dish.readthedocs.io/en/latest/)
* [GitHub Repository](https://github.com/dullbananas/dish)
