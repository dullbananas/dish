Extension Interface
===================

The Dish shell is extended through modules. These modules must have a function
called ``register_extension``, which must accept the ``Dish`` objects as an
argument. The function has to initialize the extension by setting properties on
the ``Dish`` object, which are listed below. If you still don't understand how
to write extensions, you can read the `source code
<https://github.com/dullbananas/dish/tree/master/dish/ext>`_ of the built-in
extensions as an example.

.. autoattribute:: dish.Dish.start_tag_handlers

.. autoattribute:: dish.Dish.end_tag_handlers

.. autoattribute:: dish.Dish.prompt_predicates
