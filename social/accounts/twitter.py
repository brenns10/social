"""Twitter Account abstraction."""

import re
import requests
from lxml import html

from . import Account

_URL_RE = re.compile(r'https?://(www.)?twitter.com/(?P<username>\w+)/?\Z')


class TwitterAccount(Account):

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
            raise ValueError('No usable parameters')

    def expand(self, info):
        url = 'https://twitter.com/%s' % self._username
        page = requests.get(url)
        tree = html.fromstring(page.text)

        for anchor in tree.xpath(r'//a[contains(@rel,"me")]'):
            yield {'url': anchor.attrib['title']}

    @staticmethod
    def match(**options):
        return (
            'url' in options
            and _URL_RE.match(options['url'])
        )

    @staticmethod
    def shortname():
        return 'twitter'

    def __str__(self):
        return 'TwitterAccount(username=%r)' % self._username

    def __hash__(self):
        return hash(self._username)

    def __eq__(self, other):
        return type(other) is TwitterAccount and self._username == other._username
