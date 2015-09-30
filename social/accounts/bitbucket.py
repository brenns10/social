"""
**BitbucketAccount**

Represents a person's Bitbucket account.

- Matches links that look like Bitbucket profiles.
- Expands to the URLs provided in profile.
- Use on command line: ``bitbucket:user``.
"""

import re
import requests
from lxml import html

from . import Account

_URL_RE = re.compile(r'https?://(www.)?bitbucket.com/(?P<username>\w+)/?')


class BitbucketAccount(Account):

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
        # Load profile page
        url = 'https://bitbucket.org/%s' % self._username
        page = requests.get(url)
        tree = html.fromstring(page.text)

        # Save info
        info['usernames'] = self._username
        for title in tree.xpath(r'//section[@id="user-profile"]/h1'):
            info['name'] = title.text.strip()

        # Get more links.
        for anchor in tree.xpath(r'//a[contains(@rel, "me")]'):
            yield {'url': anchor.attrib['href']}

    @staticmethod
    def match(**options):
        return (
            'url' in options
            and _URL_RE.fullmatch(options['url'])
        )

    @staticmethod
    def shortname():
        return 'bitbucket'

    def __str__(self):
        return 'BitbucketAccount(username=%r)' % self._username

    def __hash__(self):
        return hash(self._username)

    def __eq__(self, other):
        return type(other) is BitbucketAccount and self._username == other._username
