"""Semantic Versioning Helper for Python
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _error as error
from ._api import last
from ._api import last as last_version
from ._version import Version, VERSION_PART_MAX
from ._version_range import VersionRange
from ._error import InvalidVersionIdentifier, InvalidComparisonOperator, InvalidCondition, InvalidRequirementString, \
    InvalidVersionRangeIdentifier
