"""setup.py
"""
from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='semaver',
    version='0.2.1',
    author='Oleksandr Shepetko',
    author_email='a@shepetko.com',
    description='Semantic Versioning Helper for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ashep/semaver',
    download_url='https://github.com/ashep/semaver/archive/master.zip',
    packages=find_packages(),
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
