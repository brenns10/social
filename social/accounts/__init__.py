"""Import and register all account types."""

from abc import ABCMeta, abstractmethod

__accounts__ = dict()


class ABCRegistrar(ABCMeta):

    def __init__(cls, name, bases, clsdict):
        super(ABCRegistrar, cls).__init__(cls, name, bases, clsdict)
        __accounts__[cls.__name__] = cls


class Account(object):

    __metaclass__ = ABCRegistrar

    @staticmethod
    @abstractmethod
    def match(url):
        pass

    @abstractmethod
    def expand(self, url, info):
        pass
