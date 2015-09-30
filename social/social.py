"""Contains core network code."""

from __future__ import print_function, division
from collections import deque

# This import loads all social account modules (and sadly puts them into the
# current namespace).
from accounts import *
# This actually imports the stuff from accounts/__init__.py we want.
from accounts import Account, account_for
from info import DemographicInfo
import logging
log = logging.getLogger('social')


def account_slug(slug):
    acct_type, username = slug.split(':', 1)
    for cls in Account.__subclasses__():
        if acct_type == cls.__name__ or acct_type == cls.shortname():
            return cls(username=username)


def build_network(initial_account):
    """Given an initial account, attempt to return all other accounts."""
    visit_queue = deque([initial_account])
    accounts = set([initial_account])
    info = DemographicInfo()

    # Dijkstra's Algorithm, anyone?
    while visit_queue:
        account = visit_queue.popleft()
        print(account)
        for breadcrumbs in account.expand(info):
            log.debug(breadcrumbs)
            new_account = account_for(**breadcrumbs)
            if new_account is not None and new_account not in accounts:
                accounts.add(new_account)
                visit_queue.append(new_account)

    print(info)
    return accounts


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Social network expander')
    parser.add_argument('account', type=str, help='starting social account')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='enable logging output')
    args = parser.parse_args()

    if args.verbose:
        log.addHandler(logging.StreamHandler())
        log.setLevel(logging.DEBUG)

    acct = account_slug(args.account)
    build_network(acct)
