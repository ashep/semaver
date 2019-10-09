# SemaVer

SemaVer is a simple library for Python that helps to work with versions using 
[semantic versioning notation].


## Build status

[![Build Status](https://travis-ci.org/ashep/semaver.svg?branch=master)](https://travis-ci.org/ashep/semaver)
[![Coverage](https://codecov.io/gh/ashep/semaver/branch/master/graph/badge.svg)](https://codecov.io/gh/ashep/semaver)


## Requirements

[Python] >=3.5


## Installation

```bash
pip install semaver
```

## Usage


### Version objects

To create a version object, instantiate the `Version` class and pass version 
identifier as a first constructor's argument: 

```python
from semaver import Version

v1_0_0 = Version('1.0.0')
```

Valid version identifiers can be found at [semver.org](https://semver.org/). 
Please note that currently *SemaVer* does not support [pre-release] and 
[build metadata] specs.

All non-specified parts of the version identifier counts as zeroes, i. e. 
`'1' == '1.0' == '1.0.0'`.


### Compare versions

You may compare versions using regular [Python comparison operators]:

```python
from semaver import Version

v1_0 = Version('1.0')
v1_0_0 = Version('1.0.0')
v1_0_1 = Version('1.0.1')

assert v1_0 == v1_0_0  # True
assert v1_0 != v1_0_0  # False

assert v1_0 < v1_0_1  # True
assert v1_0 <= v1_0_1  # True
assert v1_0 > v1_0_1  # False
assert v1_0 >= v1_0_1  # False

# Or using plain strings

assert v1_0 == '1'  # True
assert v1_0 == '1.0'  # True
assert v1_0 == '1.0.0'  # True
```


### Adding and subtracting versions

```python
from semaver import Version

print(Version('1.0.0') + Version('0.1.1'))  # '1.1.1'
```

```python
from semaver import Version

print(Version('2.0.1') - Version('1.0.1'))  # '1.0.0'
```


### Version range objects

Instance of `VersionRange` represents a version range. First argument of the
constructor is a version range identifier. 

```python
from semaver import VersionRange

VersionRange('1.x')
```

Following formats are supported.

- [PEP-440 version specifiers] except `~=` and `===` clauses.
- [NPM version range syntax].
  
For example, each item of the following list shows equal version range 
identifiers: 

- `1.x`, `1.*`, `^1`, `>=1,<2`.
- `^1.1`, `>=1.1,<2`.
- `1.0.x`, `1.0.*`, `~1`, `~1.0`.


## Checking if a version is in a range

```python
from semaver import Version, VersionRange

v1_2_3 = Version('1.2.3')
v1_x = VersionRange('1.x')
v2_x = VersionRange('2.x')

assert v1_2_3 in v1_x  # True
assert v1_2_3 in v2_x  # False

# Or using plain strings

assert '1.2.3' in v1_x  # True
assert '1.2.3' in v2_x  # False
```

## Checking if a range is in a range

```python
from semaver import VersionRange

v1_to_3 = VersionRange('>=1,<=3')
v2_x = VersionRange('2.x')

assert v2_x in v1_to_3  # True
assert v1_to_3 in v2_x  # False

# Or using plain strings

assert '2.x' in v1_to_3  # True
assert '>=1,<=3' in v2_x  # False
```


## Testing

```bash
tox
```


## Contributing

See the [CONTRIBUTING.md] file for details.


## Changelog

See the [CHANGELOG.md] file for details.


## Support

If you have any issues or enhancement proposals feel free to report them via 
project's [Issue Tracker](https://github.com/ashep/semaver/issues). 


## Authors

* [Oleksandr Shepetko](https://shepetko.com) -- initial work.


## License

This project is licensed under the MIT License. See the [LICENSE.md] 
file for details.


[semantic versioning notation]: https://semver.org/

[Python]: https://python.org

[pre-release]: https://semver.org/#spec-item-9

[build-metadata]: https://semver.org/#spec-item-10

[Python comparison operators]:
    https://docs.python.org/3/reference/expressions.html#comparisons

[PEP-440 version specifiers]:
    https://www.python.org/dev/peps/pep-0440/#version-specifiers

[NPM version range syntax]:
    https://docs.npmjs.com/about-semantic-versioning#using-semantic-versioning-to-specify-update-types-your-package-can-accept

[CONTRIBUTING.md]: CONTRIBUTING.md

[CHANGELOG.md]: CHANGELOG.md

[LICENSE.md]: LICENSE.md
