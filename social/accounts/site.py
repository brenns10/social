"""Personal website abstraction."""

import re
import requests
from lxml import html

from . import Account, account_for

_URL_RE = re.compile(r'https?://[\w-]+(\.[\w-]+)+/?')


class PersonalSite(Account):

    def __init__(self, url=None):
        if url is not None:
            self._url = url
        else:
            raise ValueError("That doesn't quite look like a personal site.")

    def expand(self, info):
        page = requests.get(self._url)
        tree = html.fromstring(page.text)
        for anchor in tree.xpath('//a'):
            url = anchor.attrib['href']
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
            and _URL_RE.fullmatch(options['url'])
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