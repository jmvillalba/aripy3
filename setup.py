#!/usr/bin/env python

#
# Copyright (c) 2013, Digium, Inc.
#

import os

from setuptools import setup

setup(
    name="aripy3",
    version="0.3.0",
    license="BSD 3-Clause License",
    description="Asyncronous library for accessing the Asterisk REST Interface",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.rst")).read(),
    author="AVOXI, Inc.",
    author_email="darren.sessions@avoxi.com",
    url="https://github.com/AVOXI/aripy3",
    packages=["aripy3"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraripy3es :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    tests_require=["coverage", "httpretty", "nose", "tissue"],
    install_requires=["swaggerpy3"],
)
