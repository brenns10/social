"""
.. automodule:: social.accounts.github
.. automodule:: social.accounts.site
.. automodule:: social.accounts.twitter
.. automodule:: social.accounts.so
"""

from abc import ABCMeta, abstractmethod
from six import with_metaclass

__all__ = ['github', 'site', 'twitter', 'so']


def account_for(**breadcrumbs):
    """Return the first account the breadcrumbs match."""
    for cls in Account.__subclasses__():
        if cls.match(**breadcrumbs):
            return cls(**breadcrumbs)


class Account(with_metaclass(ABCMeta, object)):
    """
    Base class for all types of social networking accounts.

    In order for an Account to be considered in the search, it must satisfy two
    requirements:

    1. It must be a direct subclass of Account.  As of right now, only direct
       subclasses are included.  However, this may change if I find it
       convenient to include intermediate classes for utility.
    2. It must have been imported prior to the search, so that the class name is
       registered in ``Account.__subclasses__()``.

    *Constructor*

    :param dict breadcrumbs: The breadcrumbs object to construct the account
      from.  If meth:`match()` returned truthy, this should succeed.  If
      :meth:`match()` returned false-y, it may still return an instance, but the
      returned account is less "guaranteed" to be definitely the same person's.

    :raises ValueError: The constructor shall raise ``ValueError`` in the case
      that the breadcrumbs cannot be resolved into an account instance.  This
      should not happen if :meth:`match()` returned truthy.
    """

    @abstractmethod
    def __init__(self, *breadcrumbs):
        pass

    @staticmethod
    @abstractmethod
    def shortname():
        """
        Return the name used on the command line.

        Command line arguments are passed in ``key:value`` style.  This should
        return the key that users can use on the command line to specify a
        username for this account.
        """
        pass

    @staticmethod
    @abstractmethod
    def match(*breadcrumbs):
        """
        Return truthy if the breadcrumbs match the account.

        The breadcrumbs are described in detail in the documentation.

        :param dict breadcrumbs: Key/value breadcrumbs to attempt to match.
        :return: Truthy if the breadcrumbs can be turned into an instance.
        """
        pass

    @abstractmethod
    def expand(self, info):
        """
        Return an iterable of breadcrumb dicts!

        :param info: A dictionary that should contain information about the
          person.  It should be updated with any information you come across,
          and you may want to use any info in it to help narrow down your
          search.
        :return: An iterable of breadcrumb dictionaries that the search will try
          to match for new accounts.
        """
        pass

    @abstractmethod
    def __hash__(self):
        """
        Return the hash, so the Account may be kept in a set/dict.
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Return the string representation of this account.

        This must return ``"ClassName(necessary=args)"``, such that if you
        eval'd it with the correct imports, you would get a valid account
        object.  The implementation should prefer the easy arguments,
        e.g. username.
        """
