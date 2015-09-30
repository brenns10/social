"""
**EmailAccount**

Represents an email account.  For the most part, this just exists to make it
easier to parse ``mailto:...`` email address links, so that other plugins don't
have to be modified.

- Matches ``mailto:...`` links.
- Expands to a single ``{'email': '...'}`` breadcrumb.
- Use on command line: ``email:example@example.com``.
"""

import re
from urllib.parse import unquote

from . import Account

_URL_RE = re.compile(r'mailto:(?P<email>.*)')


class EmailAccount(Account):

    def __init__(self, username=None, email=None, url=None, **_):
        if username is not None:
            self._email = username
        elif email is not None:
            self._email = email
        elif url is not None:
            match = _URL_RE.fullmatch(url)
            if match:
                # some places quote emails to hide them from scrapers :)
                self._email = unquote(match.group('email'))
            else:
                raise ValueError('No username match.')
        else:
            raise ValueError('No usable parameters')

    def expand(self, info):
        emails = info.get('emails', set())
        emails.add(self._email)
        info['emails'] = emails
        yield {'email': self._email}

    @staticmethod
    def match(**options):
        return (
            'url' in options
            and _URL_RE.fullmatch(options['url'])
        )

    @staticmethod
    def shortname():
        return 'email'

    def __str__(self):
        return 'EmailAccount(email=%r)' % self._email

    def __hash__(self):
        return hash(self._email)

    def __eq__(self, other):
        return type(other) is EmailAccount and self._email == other._email
