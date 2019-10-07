"""Semantic Versioning Helper for Python
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import SupportsInt
import re
from . import _error

VERSION_PART_MAX = 9999

_VERSION_RE = re.compile(r'^(\d+)(?:\.(\d+)(?:\.(\d+))?)?$')


class Version(SupportsInt):
    def __init__(self, version=0):
        """
        Init

        :param _Union[str, int, Version] version: version
        """
        self._major = self._minor = self._patch = 0

        if isinstance(version, Version):
            self._major = version.major
            self._minor = version.minor
            self._patch = version.patch
        elif isinstance(version, str):
            match = _VERSION_RE.findall(str(version))
            if not match:
                raise _error.InvalidVersionIdentifier(version)
            self.major, self.minor, self.patch = match[0][0], match[0][1], match[0][2]
        elif isinstance(version, int):
            version = '{:012d}'.format(version)
            self.major = version[:4].strip()
            self.minor = version[4:8].strip()
            self.patch = version[8:].strip()
        else:
            raise TypeError('Version identifier must be a str or Version instance, not {}'.format(type(version)))

    @property
    def major(self) -> int:
        return self._major

    @major.setter
    def major(self, value: int):
        value = int(value or 0)
        if value < 0 or value > VERSION_PART_MAX:
            raise ValueError('Major number must be between 0 and {}'.format(VERSION_PART_MAX))
        self._major = value

    @property
    def minor(self) -> int:
        return self._minor

    @minor.setter
    def minor(self, value: int):
        value = int(value or 0)
        if value < 0 or value > VERSION_PART_MAX:
            raise ValueError('Minor number must be between 0 and {}'.format(VERSION_PART_MAX))
        self._minor = value

    @property
    def patch(self) -> int:
        return self._patch

    @patch.setter
    def patch(self, value: int):
        value = int(value or 0)
        if value < 0 or value > VERSION_PART_MAX:
            raise ValueError('Patch number must be between 0 and {}'.format(VERSION_PART_MAX))
        self._patch = value

    def __str__(self) -> str:
        return '{}.{}.{}'.format(self._major, self._minor, self._patch)

    def __repr__(self) -> str:
        return "{}('{}')".format(self.__class__.__name__, str(self))

    def __hash__(self) -> int:
        return int(self)

    def __int__(self) -> int:
        return int('{:04d}{:04d}{:04d}'.format(self._major, self._minor, self._patch))

    def __lt__(self, other) -> bool:
        return int(self) < int(Version(other))

    def __le__(self, other) -> bool:
        return int(self) <= int(Version(other))

    def __gt__(self, other) -> bool:
        return int(self) > int(Version(other))

    def __ge__(self, other) -> bool:
        return int(self) >= int(Version(other))

    def __eq__(self, other) -> bool:
        return int(self) == int(Version(other))

    def __ne__(self, other) -> bool:
        return int(self) != int(Version(other))

    def __add__(self, other):
        return Version(int(self) + int(other))

    def __sub__(self, other):
        return Version(int(self) - int(other))


