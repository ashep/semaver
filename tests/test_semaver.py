"""Semantic Versioning Helper for Python Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from semaver import error, Version, VersionRange, VERSION_PART_MAX, last_version

_MAX_MINOR_PATCH = '{}.{}'.format(*[VERSION_PART_MAX for _ in range(2)])


class TestSemaver:
    def test_version(self):
        v1 = Version('1')
        v1_0_1 = Version('1.0.1')
        v1_1 = Version('1.1')
        v1_1_1 = Version('1.1.1')
        v2 = Version('2')

        # __int__(), __hash__(), __str__()
        assert int(v1) == hash(v1) == 100000000
        assert str(v1) == '1.0.0'
        assert int(v1_0_1) == hash(v1_0_1) == 100000001
        assert str(v1_0_1) == '1.0.1'
        assert int(v1_1) == hash(v1_1) == 100010000
        assert str(v1_1) == '1.1.0'
        assert int(v1_1_1) == hash(v1_1_1) == 100010001
        assert str(v1_1_1) == '1.1.1'
        assert int(v2) == hash(v2) == 200000000
        assert str(v2) == '2.0.0'

        # Equal
        assert v1 == 100000000
        assert v1 == '1'
        assert v1 == '1.0'
        assert v1 == '1.0.0'
        assert v1_0_1 == 100000001
        assert v1_0_1 == '1.0.1'
        assert v1_1 == 100010000
        assert v1_1 == '1.1'
        assert v1_1 == '1.1.0'
        assert v1_1_1 == 100010001
        assert v1_1_1 == '1.1.1'
        assert v2 == 200000000
        assert v2 == '2'
        assert v2 == '2.0'
        assert v2 == '2.0.0'

        # Not equal
        assert v1 != v1_0_1 != v1_1 != v2

        # Less, less or equal
        assert v1 < v1_0_1 < v1_1 < v2
        assert v1 <= v1_0_1 <= v1_1 <= v2

        # Greater, greater or equal
        assert v2 > v1_1 > v1_0_1 > v1
        assert v2 >= v1_1 >= v1_0_1 >= v1

        # Add
        assert v1 + v1_0_1 + v1_1 + v1_1_1 + v2 == Version('6.2.2')

        # Subtract
        assert Version('6.2.2') - v2 - v1_1_1 - v1_1 - v1_0_1 - v1 == Version('0.0.0')

    def test_invalid_version_identifier(self):
        for v in ('-1', 'a'):
            with pytest.raises(error.InvalidVersionIdentifier):
                Version(v)

        for v in (None, list(), tuple(), dict()):
            with pytest.raises(TypeError):
                Version(v)

    def test_invalid_version_part(self):
        v = Version()

        for p in ('major', 'minor', 'patch'):
            with pytest.raises(ValueError):
                setattr(v, p, VERSION_PART_MAX + 1)

    def test_last_version(self):
        v1 = Version('1.2.3')
        v2 = Version('4.5.6')

        assert last_version([v1, v2]) == v2
        assert last_version([v1, v2], VersionRange('1')) == v1
        assert last_version([v1, v2], VersionRange('4')) == v2

    def test_version_range(self):
        assert VersionRange('') == \
               VersionRange('*') == \
               VersionRange('*.*') == \
               VersionRange('*.*.*') == \
               VersionRange('x') == \
               VersionRange('x.x') == \
               VersionRange('x.x.x') == \
               VersionRange('>=0') == \
               VersionRange('<={}.{}.{}'.format(*[VERSION_PART_MAX for _ in range(3)]))

        assert VersionRange('1') == \
               VersionRange('1.*') == \
               VersionRange('1.*.*') == \
               VersionRange('1.x') == \
               VersionRange('1.x.x') == \
               VersionRange('^1') == \
               VersionRange('^1.0') == \
               VersionRange('==1') == \
               VersionRange('==1.x') == \
               VersionRange('==1.*') == \
               VersionRange('==1.x.x') == \
               VersionRange('==1.*.*') == \
               VersionRange('>=1,<=1.{}'.format(_MAX_MINOR_PATCH)) == \
               VersionRange('>0.{},<2'.format(_MAX_MINOR_PATCH))

        assert VersionRange('1.0') == \
               VersionRange('1.0.*') == \
               VersionRange('1.0.x') == \
               VersionRange('~1') == \
               VersionRange('~1.0') == \
               VersionRange('==1.0.x') == \
               VersionRange('==1.0.*') == \
               VersionRange('>=1.0,<=1.0.{}'.format(VERSION_PART_MAX)) == \
               VersionRange('>0.{},<1.1'.format(_MAX_MINOR_PATCH))

        assert VersionRange('1.0.0') == \
               VersionRange('==1.0.0')

    def test_version_in_range(self):
        vr1_x = VersionRange('1.x')
        vr1_1_x = VersionRange('1.1.x')

        v1 = Version('1')
        v1_1 = Version('1.1')
        v1_1_1 = Version('1.1.1')

        assert v1 in vr1_x
        assert v1_1 in vr1_x
        assert v1_1_1 in vr1_x

        assert v1 not in vr1_1_x
        assert v1_1 in vr1_1_x
        assert v1_1_1 in vr1_1_x

    def test_range_in_range(self):
        vr1_x = VersionRange('1.x')

        assert VersionRange('1.2.3') in vr1_x
        assert '1.2.3' in vr1_x
        assert [VersionRange('1.2.3'), VersionRange('1.3.2')] in vr1_x

        assert VersionRange('3.2.1') not in vr1_x
        assert [VersionRange('3.2.1'), VersionRange('1.3.2')] not in vr1_x

    def test_range_str(self):
        assert str(VersionRange('1.0.0')) == '==1.0.0'
        assert str(VersionRange('>=1')) == '>=1.0.0'
        assert str(VersionRange('1.0')) == '==1.0.*'
        assert str(VersionRange('1')) == '==1.*'
        assert str(VersionRange('>=1.2.3,<=3.2.1')) == '>=1.2.3,<=3.2.1'
        assert str(VersionRange('>1.2.3,<3.2.1')) == '>=1.2.4,<=3.2.0'

    def test_range_hash(self):
        vr1_x = VersionRange('1.x')

        assert hash(vr1_x) == int(vr1_x)

    def test_invalid_version_range_identifier(self):
        with pytest.raises(error.InvalidVersionRangeIdentifier):
            VersionRange('<1,>2')

        with pytest.raises(error.InvalidVersionRangeIdentifier):
            VersionRange('a.b.c')

    def test_invalid_init(self):
        for v in (['1.2.3'], ('1.2.3',)):
            with pytest.raises(TypeError):
                VersionRange(v)
