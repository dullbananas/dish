Installation and Setup
======================


Installing the Dish package
---------------------------

.. highlight:: shell-session

Dish currently has not been released, so it's not possible to install it with
pip.

To install the master branch of Dish::

   $ git clone https://github.com/dullbananas/dish.git
   $ cd dish
   $ python3 setup.py install --user


Writing the configuration script
--------------------------------

.. highlight:: python3

After you install Dish, you can't run it yet; you have to create the
configuration script. The way you configure Dish is a lot like Flask. Here is an
example::

   #!/usr/bin/env python3
   from dish import Dish

   dish = Dish()

   if __name__ == '__main__':
       dish.run()

Name the file "dish" and put in one of the directories in ``PATH`` and run the
``dish`` command. You should see a dollar sign prompt appear. Type ``exit`` to
exit Dish.

.. note::
   Do not name this script "dish.py", or else it will try to import itself.
