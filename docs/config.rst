Configuration
=============

.. highlight:: python3


Dish is very easy to configure. To set a configuration value, you simply just do
this, where ``dish`` is a Dish object::

   dish.config['NAME'] = 'value'


Registering Extensions
----------------------

Extensions can do many things in Dish, such as adding new XML tags that can be
used in PS1. This is how you register an extension::

   import my_extension
   dish.register_extension(my_extension)

Some extensions have additional parameters you can pass to the
``register_exetnsion`` method.


Configuring the Prompt String
-----------------------------

The ``PS1`` string is configured like this::

   dish.config['PS1'] = '$ '

Special styles and values are inserted using XML tags. Dish comes with a built-in
extension called ``ansicolor``, which allows you to use ANSI colors in your
prompt by using CSS color names. Here is an example::

   from dish.ext import ansicolor
   dish.register_extension(ansicolor)
   dish.config['PS1'] = '<color fg="green">$</color> '

.. note::
   Due to `a bug in prompt_toolkit
   <https://github.com/prompt-toolkit/python-prompt-toolkit/issues/1011>`_, some
   color names do not work and will cause a ``ValueError``.
