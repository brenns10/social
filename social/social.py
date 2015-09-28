"""Contains core network expansion code."""

from __future__ import print_function, division
from collections import deque

from accounts import *
from accounts import Account


def account_for(**breadcrumbs):
    """Return the first account the breadcrumbs match."""
    for cls in Account.__subclasses__():
        if cls.match(**breadcrumbs):
            return cls(**breadcrumbs)


def account_slug(slug):
    acct_type, username = slug.split(':', 1)
    for cls in Account.__subclasses__():
        if acct_type == cls.__name__ or acct_type == cls.shortname():
            return cls(username=username)


def build_network(initial_account):
    """Given an initial account, attempt to return all other accounts."""
    visit_queue = deque([initial_account])
    accounts = set([initial_account])
    info = dict()

    # Dijkstra's Algorithm, anyone?
    while visit_queue:
        account = visit_queue.popleft()
        print(account)
        for breadcrumbs in account.expand(info):
            new_account = account_for(**breadcrumbs)
            if new_account is not None and new_account not in accounts:
                accounts.add(new_account)
                visit_queue.append(new_account)

    return accounts


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Must provide starting account.')
        sys.exit(1)
    else:
        acct = account_slug(sys.argv[1])
        build_network(acct)
