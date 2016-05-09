#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Log colorizer
"""
import sys
from setuptools import setup, find_packages

VERSION = "1.8.2"

requires = []

if sys.platform == 'win32':
    requires.append('colorama')

options = dict(
    name="log_colorizer",
    version=VERSION,
    description="A color formater for python logging",
    long_description=__doc__,
    author="Kozea",
    author_email="florian.mounier@kozea.fr",
    license="BSD",
    platforms="Any",
    use_2to3=True,
    packages=find_packages(),
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules"])

setup(**options)
