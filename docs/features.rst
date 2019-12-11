Features
========


Auto Suggestion
---------------

Auto suggestion works similar to the way it works in the fish shell. In Dish, it
automatically gets the available options for the command you are typing by
running it with ``--help`` and parsing its output. In other words, Dish provides
partial auto suggesion support for all commands without any configuration
needed. Dish also auto suggests file names.

Using auto suggestion is simple. As you type commands, the suggestions will
appear in grey. Press the right arrow key to use them.

.. versionadded:: 0.1
   Added auto suggestion. Options are parsed from ``--help`` output, and
   filenames are also suggested.


Syntax Highlighting
-------------------

Dish syntax highlights commands as you type. In version 0.0, a Bash lexer was
used. In version 0.1, a custom lexer is now used, which currently only colors
comments.


Aliases
-------

Dish allows you to set aliases using the ``ALIASES`` config option. Here is an
example::

   dish.config['ALIASES'] = {
       'ls': 'ls --color',
       'g': 'git',
   }
