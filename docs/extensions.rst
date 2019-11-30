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

``<git-branch/>``
   Returns the active Git branch.

These are the prompt predicates that it defins:

``git``
   Returns ``True`` if the current working directory is in a Git repository.
