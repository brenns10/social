"""Contains core network expansion code."""

from __future__ import print_function, division
from collections import deque

import accounts


def account_for(url):
    """Return the first account the URL matches."""
    for name, cls in accounts.__accounts__:
        if cls.match(url):
            return cls(url)

def build_network(initial_account, options=None):
    """Given an initial account, attempt to return all other accounts."""
    visit_queue = deque([initial_account])
    accounts = set([initial_account])
    info = dict()

    # Dijkstra's Algorithm, anyone?
    while visit_queue:
        account = visit_queue.popleft()
        for url in account.expand(info):
            new_account = account_for(url)
            if new_account not in accounts:
                accounts.add(new_account)
                visit_queue.append(new_account)

    return accounts
