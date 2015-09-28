"""Import and register all account types."""

from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def __init__(self, *breadcrumbs):
        """
        Return an Account object corresponding to the breadcrumbs.

        This should only be called if "match" returned truthy about matching the
        breadcrumbs.  Otherwise, you're just mean.
        """
        pass

    @staticmethod
    @abstractmethod
    def match(*breadcrumbs):
        """
        Return truthy if the breadcrumbs match the account.

        The breadcrumbs are described below, but match functions should be
        written to gracefully accept more or less keys in the breadcrumbs.

        :param dict breadcrumbs: Dictionary containing at least one of the
          following breadcrumbs:
          - url: A URL that probably points to their profile.
          - email: An email that could be used to find the profile.
          - username: A username for the account.
        """
        pass

    @abstractmethod
    def expand(self, info):
        """
        Return an iterable of breadcrumb structs!

        :param info: A dictionary that should contain information about the
          person.  It should be updated with any information you come across,
          and you may want to use any info in it to help narrow down your
          search.
        """
        pass
