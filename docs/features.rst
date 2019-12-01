Features
========


Auto Suggestion
---------------

Auto suggestion works similar to the way it works in the fish shell. In Dish, it
automatically gets the available options for the command you are typing by
running it with ``--help`` and parsing its output. In other words, Dish provides
partial auto suggesion support for all commands without any configuration
needed.

.. versionadded:: 0.1
   Options are parsed from ``--help`` output.


Aliases
-------

Dish allows you to set aliases using the ``ALIASES`` config option. Here is an
example::

   dish.config['ALIASES'] = {
       'ls': 'ls --color',
       'g': 'git',
   }
