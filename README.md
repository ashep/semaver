# SemaVer

Semaver is a simple library for Python that helps to work with versions using 
[semantic versioning notation](https://semver.org/).


## Build status

[![Build Status](https://travis-ci.org/ashep/semaver.svg?branch=master)](https://travis-ci.org/ashep/semaver)
[![Coverage](https://codecov.io/gh/ashep/semaver/branch/master/graph/badge.svg)](https://codecov.io/gh/ashep/semaver)


## Requirements

[Python](https://python.org) >=3.5


## Installation

```bash
pip install semaver
```

## Usage


### Create version object

```python
from semaver import Version

v1_0_0 = Version('1.0.0')

# or

v1_0 = Version('1.0')  # The same as above

# or even

v1 = Version('1')  # The same as above
```


### Compare versions

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
```


### Compare version against string

```python
from semaver import Version

v1_0 = Version('1.0')
v1_0_0 = Version('1.0.0')
v1_0_1 = Version('1.0.1')

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


### Create version range object

```python
from semaver import VersionRange

VersionRange('1')
```


## Documentation

To do.


## Testing

```bash
tox
```


## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.


## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for details.


## Roadmap

* Cleanup existing code.
* Write missing comments in code.
* Write tests.
* Write documentation.
* Finish this readme.


## Support

If you have any issues or enhancement proposals feel free to report them via 
project's [Issue Tracker](https://github.com/ashep/semaver/issues). 


## Authors

* [Oleksandr Shepetko](https://shepetko.com) -- initial work.


## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) 
file for details.
