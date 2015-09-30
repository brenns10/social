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

Documentation
-------------

Information on using and extending this program can be found at its
documentation page: http://stephen-brennan.com/social/

Contributing
------------

I'm mainly a Python 3 developer, but I have tried the code on Python 2 and fixed
a few things so that it runs there as well.  Feel free to create an issue for
compatibility problems and I'll try to address it.  This module is pure Python
and I see no reason why it shouldn't support 2 and 3.

I'm also glad to accept pull requests with new social network types.  See the
"Contributing" section of the documentation for more info.

Future Work
-----------

- I'm intending to add many new plugins as time allows, e.g.:
    - Bitbucket
    - Slideshare
    - LinkedIn
    - Others?  Feel free to suggest in issue or create it and PR it!
- I'll probably create an `Info` class that manages information about the user
  that the plugins dig up (better than passing around a dict).
- I'd like to add an OAuth credential storage API so that plugins can use a
  social network APIs to get more information.  Very exciting.
- I'd also like to add a second phase to the search.  It will take the person's
  known usernames, and search for under those usernames in all the account types
  it hasn't found yet.  Then, it will present these to the user and prompt
  whether or not it belongs to them.  If so, it will continue the search.

License
-------

This project is under the Revised BSD license.  See [LICENSE.txt](LICENSE.txt)
for details.
