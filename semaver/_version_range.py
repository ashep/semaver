"""Semantic Versioning Helper for Python
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import re
from . import _error
from ._version import Version, VERSION_PART_MAX

_VERSION_RANGE_RE_V1 = re.compile(r'(==|<=|>=|>|<|~|\^)\s*(\d+)(?:\.(\d+)(?:\.(\d+))?)?')
_VERSION_RANGE_RE_V2 = re.compile(r'^(\d+|x|\*)(?:\.(\d+|x|\*)(?:\.(\d+|x|\*))?)?$')
_MAX_VERSION_STR = '{}.{}.{}'.format(VERSION_PART_MAX, VERSION_PART_MAX, VERSION_PART_MAX)


class VersionRange:
    def __init__(self, v_range=None):
        """
        :param _Union[str, VersionRange] v_range: version range
        """
        self._minimum = Version('0.0.0')
        self._maximum = Version('{}.{}.{}'.format(VERSION_PART_MAX, VERSION_PART_MAX, VERSION_PART_MAX))

        if not v_range or v_range in ('*', 'x'):
            return

        if isinstance(v_range, str):
            match = _VERSION_RANGE_RE_V1.findall(v_range)
            if match:
                for m in match:
                    op = m[0]
                    if op in ('>', '>='):
                        self._minimum.major = m[1]
                        self._minimum.minor = m[2] or 0
                        self._minimum.patch = m[3] or 0
                        if op == '>':
                            self._minimum += 1
                    elif op in ('<', '<='):
                        self._maximum.major = m[1]
                        self._maximum.minor = m[2] or 0
                        self._maximum.patch = m[3] or 0
                        if op == '<':
                            self._maximum -= 1
                    elif op == '==':
                        if m[1]:
                            self._minimum.major = self._maximum.major = m[1]
                        if m[2]:
                            self._minimum.minor = self._maximum.minor = m[2]
                        if m[3]:
                            self._minimum.patch = self._maximum.patch = m[3] or 0
                    elif op == '^':
                        self._minimum.major = self._maximum.major = m[1]
                        self._minimum.minor = m[2] or 0
                        self._minimum.patch = m[3] or 0
                    elif op == '~':
                        self._minimum.major = self._maximum.major = m[1]
                        self._minimum.minor = self._maximum.minor = m[2] or 0
                        self._minimum.patch = m[3] or 0

                if self._minimum > self._maximum:
                    raise _error.InvalidVersionRangeIdentifier(v_range)

            else:
                match = _VERSION_RANGE_RE_V2.findall(v_range)
                if match:
                    for i in range(3):
                        if match[0][i] in ('', 'x', '*'):
                            if i == 0:
                                self._minimum.major = 0
                                self._maximum.major = VERSION_PART_MAX
                            elif i == 1:
                                self._minimum.minor = 0
                                self._maximum.minor = VERSION_PART_MAX
                            elif i == 2:
                                self._minimum.patch = 0
                                self._maximum.patch = VERSION_PART_MAX
                        else:
                            if i == 0:
                                self._minimum.major = match[0][i]
                                self._maximum.major = match[0][i]
                            elif i == 1:
                                self._minimum.minor = match[0][i]
                                self._maximum.minor = match[0][i]
                            elif i == 2:
                                self._minimum.patch = match[0][i]
                                self._maximum.patch = match[0][i]
                else:
                    raise _error.InvalidVersionRangeIdentifier(v_range)

        elif isinstance(v_range, VersionRange):
            self._minimum = v_range.minimum
            self._maximum = v_range.maximum

        else:
            raise TypeError(
                'Version range identifier must be a str or VersionRange instance, got {}'.format(type(v_range)))

    @property
    def minimum(self) -> Version:
        return self._minimum

    @property
    def maximum(self) -> Version:
        return self._maximum

    def __eq__(self, other):
        return int(self) == int(VersionRange(other))

    def __contains__(self, item):
        """__contains__()
        """
        if isinstance(item, (list, tuple)):
            for i in item:
                if i not in self:
                    return False
            return True

        if isinstance(item, str):
            item = Version(item)

        if isinstance(item, Version):
            return self.minimum <= item <= self.maximum

        if isinstance(item, VersionRange):
            return self.minimum <= item.minimum and self.maximum >= item.maximum

    def __str__(self) -> str:
        """__str__()
        """
        # Exact version
        if self._minimum == self._maximum:
            return '=={}'.format(self._minimum)

        # Greater or equals version
        elif self._maximum == _MAX_VERSION_STR:
            return '>={}'.format(self._minimum)

        # Fixed major version
        elif self._minimum.major == self._maximum.major:
            # Fixed minor version
            if self._minimum.minor == self._maximum.minor:
                # Any patch version
                if self._minimum.patch == 0 and self._maximum.patch == VERSION_PART_MAX:
                    return '=={}.{}.*'.format(self._minimum.major, self._minimum.minor)

            # Any minor version
            elif self._minimum.minor == 0 and self._maximum.minor == VERSION_PART_MAX:
                # Any patch version
                if self._minimum.patch == 0 and self._maximum.patch == VERSION_PART_MAX:
                    return '=={}.*'.format(self._minimum.major)

        return '>={},<={}'.format(self._minimum, self._maximum)

    def __repr__(self) -> str:
        """__repr__()
        """
        return "{}('{}')".format(self.__class__.__name__, str(self))

    def __int__(self) -> int:
        """__int__()
        """
        return int(self._minimum) + int(self.maximum)

    def __hash__(self) -> int:
        """__hash__()
        """
        return int(self)
