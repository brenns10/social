"""
Contains DemographicInfo class, which stores info found by accounts.
"""

from collections import UserDict

class DemographicInfo(UserDict):

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].add(value)
        else:
            self.data[key] = set([value])
