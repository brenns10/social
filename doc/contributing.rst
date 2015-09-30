Contributing
============

If you're interested in adding support for a social networking account type,
check out the Extending section to get an idea of how the framework works.
Then, you may find the file ``templates/template.py`` useful for starting your
social networking account.  I'll accept pull requests with new accounts in the
``social/accounts/`` folder, just make sure you do the following:

- PEP8 your code!!  Please, even if you just run ``autopep8``.  It makes me
  happy.
- Make sure to update the ``__all__`` variable in
  ``social/accounts/__init__.py`` with your new module name so it gets
  automatically imported for the search.
