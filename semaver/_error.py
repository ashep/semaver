"""Semantic Versioning Helper for Python Errors
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class InvalidRequirementString(Exception):
    pass


class InvalidVersionIdentifier(Exception):
    def __init__(self, v: str):
        self._v = v

    def __str__(self) -> str:  # pragma: no cover
        return "'{}' is not a valid version identifier".format(self._v)


class InvalidVersionRangeIdentifier(Exception):
    def __init__(self, v_range: str):
        self._v_range = v_range

    def __str__(self) -> str:  # pragma: no cover
        return "'{}' is not a valid version range identifier".format(self._v_range)


class InvalidCondition(Exception):
    pass


class InvalidComparisonOperator(Exception):
    pass
