"""Semantic Versioning Helper for Python
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Optional, Iterable
from ._version import Version, VersionRange


def last(versions: Iterable[Version], v_range: VersionRange = None) -> Optional[Version]:
    """Get latest available version from list of versions
    """
    if not versions:
        return None

    versions = sorted(versions, key=int)

    # Return latest available
    if not v_range:
        return versions[-1]

    # Search for latest available among constraints
    filtered = [v for v in versions if v in v_range]

    return filtered[-1] if filtered else None
