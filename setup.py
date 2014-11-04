#!/usr/bin/env python
from setuptools import setup, find_packages

from fidor_python import __version__

DESCRIPTION = "Python wrapper for the Fidor Bank API"

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='fidor-python',
    version=__version__,
    packages=find_packages(exclude=[]),
    url='https://github.com/joshuakarjala/fidor-python/',
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['requests'],
)
