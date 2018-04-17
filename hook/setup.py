#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Log colorizer import hook
"""
import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

site_packages_path = get_python_lib().replace(sys.prefix + os.path.sep, '')

VERSION = "1.1.0"

options = dict(
    name="log_colorizer_hook",
    version=VERSION,
    description="Hook for auto log colorization",
    author="Kozea",
    author_email="florian.mounier@kozea.fr",
    license="BSD",
    platforms="Any",
    data_files=[(site_packages_path, ['log_colorizer_hook.pth'])],
    install_requires=['log_colorizer >= 1.8.5']
)

setup(**options)
