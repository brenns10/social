Tutorial
========

Social is pretty easy to use.  So easy, in fact, that this tutorial is almost
unnecessary.  But here it is anyway!

Getting it installed
--------------------

Since Social is in a development stage right now, I do not have a Python package
for it submitted to PyPI.  So, if you would like to try it, you'll need to
directly use the development version.  You'll need either Python 2 or Python 3,
Virtualenv, Pip, and Git.

First, clone the repository, and enter it:

.. code:: bash

          $ git clone git@github.com:brenns10/social.git
          $ cd social

Then, you'll probably want to create a "virtual environment" to hold all the
dependencies for the project.  Do so by running:

.. code:: bash

          $ virtualenv venv
          # If that doesn't work, try this:
          $ pyvenv venv

Then, enter the virtual environment, and install the required packages:

.. code:: bash

          $ . venv/bin/activate
          $ pip install -r requirements.txt

Now you should be able to run the program:

.. code:: bash

          $ python social/social.py

Running
-------

When you run the program, you give it an initial social networking account.  It
will visit that account and try to find more linked accounts.  Then it will
visit those accounts to find even more, and so forth.  To provide the first
account, you give it as a command line argument.  You give arguments in a
``key:value`` way, where the key is the name of the social network, and the
value is usually the username.  For instance, you can provide a Twitter account
like this:

.. code:: bash
          
          $ python social/social.py twitter:brenns10

When the program runs, it outputs each "social network account" on the command
line.  Happy stalking, I guess...
