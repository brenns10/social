Meta-Social Network Expander
============================

This project is a rather creepy tool that takes one of someone's social network
accounts, and attempts to expand it into a list of all of their accounts, using
publicly available information.

```bash
$ python social/social.py twitter:brenns10
TwitterAccount(username='brenns10')
PersonalSite(url='http://stephen-brennan.com')
GitHubAccount(username='brenns10')
StackOverflowAccount(username='brenns10', uid=820319)
```

Setup
-----

Clone, create a virtualenv, and install requirements:

```bash
$ git clone git@github.com:brenns10/social.git
$ cd social
$ pyvenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python social/social.py [starting:account]
```

I'm mainly a Python 3 developer, but I have tried the code on Python 2 and fixed
a few things so that it runs there as well.  Feel free to create an issue for
compatibility problems and I'll try to address it.  This module is pure Python
and I see no reason why it shouldn't support 2 and 3.

Plugin Support
--------------

- GitHub (`github:username`)
- Twitter (`twitter:username`)
- StackOverflow (`so:username:uid`)
- Personal websites (sort of)

Candidates:
- Bitbucket
- Slideshare
- LinkedIn
- Others?

Contributing
------------

I'd be glad to accept Pull Requests for more account types!  You can use the
template in the `templates` folder to get started (grep for `ReplaceMe`).  You
want to make sure all the functions work correctly (especially `__eq__`) to
prevent an infinite loop in the search.  Also, try to make sure you have PEP8
formatted code!

Perhaps most importantly, you need to update the `__all__` list in
`social/accounts/__init__.py` with the module name for your account, in order to
make it automatically import and be considered during the search.

License
-------

This project is under the Revised BSD license.  See [LICENSE.txt][] for details.
