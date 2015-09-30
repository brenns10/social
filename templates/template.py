"""
**ReplaceMe**

[Describe what your subclass does here.]

- In this bullet point, describe what your account matches.
- Here, describe what your account expands to.
- Demonstrate use on command line: ``key:value``.
"""

import re
#import requests
#from lxml import html

from . import Account

_URL_RE = re.compile(r'https?://(www.)?ReplaceMe.com/(?P<username>\w+)/?')


class ReplaceMeAccount(Account):

    def __init__(self, username=None, url=None, **_):
        if username is not None:
            self._username = username
        elif url is not None:
            match = _URL_RE.fullmatch(url)
            if match:
                self._username = match.group('username')
            else:
                raise ValueError('No username match.')
        else:
            raise ValueError('No usable parameters')

    def expand(self, info):
        return []  # TODO: fill out the expand....

    @staticmethod
    def match(**options):
        return (
            'url' in options
            and _URL_RE.fullmatch(options['url'])
        )

    @staticmethod
    def shortname():
        return 'ReplaceMe'

    def __str__(self):
        return 'ReplaceMeAccount(username=%r)' % self._username

    def __hash__(self):
        return hash(self._username)

    def __eq__(self, other):
        return type(other) is ReplaceMeAccount and self._username == other._username
