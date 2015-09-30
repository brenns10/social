"""Twitter Account abstraction."""

import re
import requests
from lxml import html

from . import Account

_URL_RE = re.compile(r'https?://(www.)?stackoverflow.com/users/(?P<id>\d+)/(?P<username>\w+)/?\Z')


class StackOverflowAccount(Account):

    def __init__(self, username=None, url=None, **_):
        if username is not None:
            self._username, self._uid = username.split(':', 1)
            self._uid = int(self._uid)
        elif url is not None:
            match = _URL_RE.match(url)
            if match:
                self._username = match.group('username')
                self._uid = int(match.group('id'))
            else:
                raise ValueError('No username match.')
        else:
            raise ValueError('No usable parameters')

    def expand(self, info):
        url = 'https://stackoverflow.com/users/%d/%s' % (self._uid,
                                                         self._username)
        page = requests.get(url)
        tree = html.fromstring(page.text)

        for anchor in tree.xpath(r'//a[@class="url"]'):
            yield {'url': anchor.attrib['href']}

    @staticmethod
    def match(**options):
        return (
            'url' in options
            and _URL_RE.match(options['url'])
        )

    @staticmethod
    def shortname():
        return 'so'

    def __str__(self):
        return 'StackOverflowAccount(username=%r, uid=%r)' % (self._username,
                                                              self._uid)

    def __hash__(self):
        return hash((self._username, self._uid))

    def __eq__(self, other):
        return type(other) is StackOverflowAccount \
            and self._username == other._username \
            and self._uid == other._uid
