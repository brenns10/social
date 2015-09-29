"""ReplaceMe abstraction."""

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
        """
        Return a generator of "breadcrumbs".

        The info parameter is a dictionary you can read and update with
        information about the person you're searching for.  So you can scrape
        names, birthdays, etc, and stick them into the dict!  Creepy, right?
        """
        return []  # TODO: fill out the expand....

    @staticmethod
    def match(**options):
        """
        Return truthy if the breadcrumbs would match this type of account.
        """
        return (
            'url' in options
            and _URL_RE.fullmatch(options['url'])
        )

    @staticmethod
    def shortname():
        """
        The name used on the CLI so that you don't have to type the class name.
        """
        return 'ReplaceMe'

    def __str__(self):
        return 'ReplaceMeAccount(username=%r)' % self._username

    def __hash__(self):
        return hash(self._username)

    def __eq__(self, other):
        """
        If you want the search to terminate, make sure this is right!
        """
        return type(other) is ReplaceMeAccount and self._username == other._username
