Builtin Extensions
==================


ansicolor
---------

This extension adds ANSI color support for prompts. It adds a new ``<color>``
tag which can be used to define ANSI colors and styles. Colors are defined using
CSS color names. This tag has the following attributes:

- ``fg``: Foreground color
- ``bg``: Background color
- ``style``: A list of space-separated styles to apply to the text:

  - ``bold``
  - ``faint``
  - ``italic``
  - ``underline``
  - ``blink``
  - ``blink2``
  - ``negative``
  - ``concealed``
  - ``crossed``

Example::

   dish.config['PS1'] = '<color bg="blue" style="italic bold">This is some text</color> <color fg="green">$</color> '


prompt_goodies
--------------

This extension adds system-related values that you can insert into your prompt.
These are the tags that it defins:

``<cwd/>``
   Returns the current working directory.

``<duration round="..."/>``
   Returns the amount of seconds it took for the previous command to run. The
   ``round`` attribute specfies the ammount of decimal places to round. If
   ``round`` is not specified, the default value, which is ``0``.

``<git-branch/>``
   Returns the active Git branch.

``<platform name="..."/>``
   Returns something from the ``platform`` module. For example,
   ``<platform name="node"/>`` returns the value of ``platform.node()``.

``<time format="..."/>``
   Returns the current time formatted using ``time.strftime()``. For example,
   ``<time format="%p"/>`` returns ``am`` or ``pm``.

``<version/>``
   Returns the installed version of Dish.

These are the prompt predicates that it defins:

``git``
   Returns ``True`` if the current working directory is in a Git repository.

.. versionchanged:: 0.1
   Git-related stuff now works with subdirectories in a repository.
