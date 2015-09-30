"""
Contains DemographicInfo class, which stores info found by accounts.
"""

from collections import UserDict
import logging
log = logging.getLogger('social.info')

class DemographicInfo(UserDict):

    def __setitem__(self, key, value):
        # Ignore empty strings...
        if type(value) is str and value == '':
            return

        log.debug('DemographicInfo: %r=%r', key, value)
        # Otherwise, do the set stuff.
        if key in self.data:
            self.data[key].add(value)
        else:
            self.data[key] = set([value])
