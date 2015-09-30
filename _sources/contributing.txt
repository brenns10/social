Contributing
============

If you're interested in adding support for a social networking account type,
check out the :ref:`extending` section to get an idea of how the framework
works.  Then, you may find the file ``templates/template.py`` useful for
starting your social networking account.  I'll accept pull requests with new
accounts in the ``social/accounts/`` folder, just make sure you do the
following:

- In your new account code file:

  - Implement all the stubbed out functions.
  - Describe the plugin as outlined in the docstring!
  - PEP8 your code!!  Please, even if you just run ``autopep8``.  It makes me
    happy.

- In ``social/accounts/__init__.py``:

  - Make sure to update the ``__all__`` variable with your new module name so it
    gets automatically imported for the search.
  - Also make sure to update the docstring with the fully documented module name
    so that its documentation is automatically generated on the plugin
    documentation page.

- Submit a pull request.
