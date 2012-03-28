#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Log colorizer
"""

from setuptools import setup, find_packages

VERSION = "1.0"


options = dict(
    name="log_colorizer",
    version=VERSION,
    description="A color formater for python logging",
    long_description=__doc__,
    author="Kozea",
    author_email="florian.mounier@kozea.fr",
    license="BSD",
    platforms="Any",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"])

setup(**options)
