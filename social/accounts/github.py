"""Github Account abstraction."""

from __future__ import print_function, division

import requests
from lxml import html

from . import Account

class GitHubAccount(Account):

    def __init__(self, username):
        self._username = username

    def expand(self, info):
        # Load their profile page.
        url = 'https://github.com/%s' % self._username
        page = requests.get(url)
        tree = html.fromstring(page.text)

        # Search for a website!
        return (a.attrib['href'] for a in tree.xpath(r'//a[@class="url"]'))
