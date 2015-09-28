"""Contains core network expansion code."""

from __future__ import print_function, division
from collections import deque

from accounts import *


def account_for(**breadcrumbs):
    """Return the first account the breadcrumbs match."""
    for cls in Account.__subclasses__:
        if cls.match(**breadcrumbs):
            return cls(**breadcrumbs)


def build_network(initial_account):
    """Given an initial account, attempt to return all other accounts."""
    visit_queue = deque([initial_account])
    accounts = set([initial_account])
    info = dict()

    # Dijkstra's Algorithm, anyone?
    while visit_queue:
        account = visit_queue.popleft()
        for breadcrumbs in account.expand(info):
            new_account = account_for(**breadcrumbs)
            if new_account not in accounts:
                accounts.add(new_account)
                visit_queue.append(new_account)

    return accounts
