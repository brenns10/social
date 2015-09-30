"""
**GitHubAccount**

Represents an account at GitHub.

- Matches a link that looks like it goes to a GitHub profile page.
- Returns the "your site" URL from the user's GitHub profile.
- Use on the command line: ``github:username``.
"""

from __future__ import print_function, division

import re
import requests
from lxml import html

from . import Account

_URL_RE = re.compile(r'https?://(www.)?github.com/(?P<username>\w+)/?\Z')


class GitHubAccount(Account):

    def __init__(self, username=None, url=None, **_):
        if username is not None:
            self._username = username
        elif url is not None:
            match = _URL_RE.match(url)
            if match:
                self._username = match.group('username')
            else:
                raise ValueError('No username match.')
        else:
            raise ValueError('No usable parameters!')

    def expand(self, info):
        # Load their profile page.
        url = 'https://github.com/%s' % self._username
        page = requests.get(url)
        tree = html.fromstring(page.text)

        # Save info
        info['usernames'] = self._username

        # Search for a website!
        for anchor in tree.xpath(r'//a[contains(@class,"url")]'):
            yield {'url': anchor.attrib['href']}
        for anchor in tree.xpath(r'//a[contains(@class, "email")]'):
            yield {'url': anchor.attrib['href']}

    @staticmethod
    def match(**options):
        return  (
            'url' in options
            and _URL_RE.match(options['url'])
        )

    @staticmethod
    def shortname():
        return 'github'

    def __str__(self):
        return 'GitHubAccount(username=%r)' % self._username

    def __hash__(self):
        return hash(self._username)

    def __eq__(self, other):
        return type(other) is GitHubAccount and self._username == other._username
