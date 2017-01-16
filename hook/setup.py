#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Log colorizer import hook
"""
import sys
import os
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

site_packages_path = get_python_lib().replace(sys.prefix + os.path.sep, '')

VERSION = "1.0.0"

options = dict(
    name="log_colorizer_hook",
    version=VERSION,
    description="Hook for auto log colorization",
    author="Kozea",
    author_email="florian.mounier@kozea.fr",
    license="BSD",
    platforms="Any",
    data_files=[(site_packages_path, ['log_colorizer_hook.pth'])],
    install_requires=['log_colorizer >= 1.8.5'])

setup(**options)
