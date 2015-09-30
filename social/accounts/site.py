"""
**PersonalSite**

This social networking "account" is supposed to represent somebody's personal
website.  The idea is that many people put their personal website in the URL
field of social network profiles, and frequently they put links to other
accounts on the frontpage of their website.

- Matches a link to a website that hos no path (or just a path of "/").

- Expands to all the links on the front page that aren't internal.

  - It actually filters to avoid links that would only match "PersonalSite"
    again, because you are already on their personal site.

- Use on the command line: ``site:http://example.com``.
"""

import re
import requests
from lxml import html

from . import Account, account_for

_URL_RE = re.compile(r'https?://[\w-]+(\.[\w-]+)+/?\Z')


class PersonalSite(Account):

    def __init__(self, url=None, username=None):
        if url is not None:
            self._url = url
        elif username is not None:
            # command line arguments are provided under the "username" argument.
            self._url = username
        else:
            raise ValueError("That doesn't quite look like a personal site.")

    def expand(self, info):
        page = requests.get(self._url)
        tree = html.fromstring(page.text)
        for anchor in tree.xpath('//a'):
            url = anchor.attrib.get('href')
            if not url:
                continue

            # Don't include links within the site.
            if url.startswith(self._url):
                continue
            acct = account_for(url=url)
            # Don't include urls that get classified as "PersonalSite", cause
            # we're on it right now :D
            if acct is None or type(acct) is PersonalSite:
                continue
            yield {'url': url}

    @staticmethod
    def match(**options):
        return (
            'url' in options
            and _URL_RE.match(options['url'])
        )

    @staticmethod
    def shortname():
        return 'site'

    def __str__(self):
        return 'PersonalSite(url=%r)' % self._url

    def __hash__(self):
        return hash(self._url)

    def __eq__(self, other):
        return type(other) is PersonalSite and self._url == other._url
