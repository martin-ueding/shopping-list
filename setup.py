#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2015 Martin Ueding <dev@martin-ueding.de>

from setuptools import setup, find_packages

setup(
    author="Martin Ueding",
    author_email="dev@martin-ueding.de",
    description="Shopping list Django application",
    license="GPL2",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",

    ],
    name="shoppinglist",
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    url="https://github.com/martin-ueding/shoppinglist",
    download_url="http://bulk.martin-ueding.de/source/shopping-list/",
    version="1.0.2",
    include_package_data = True,
    package_data = {
        '': ['*.html'],
        'shoppinglist': ['templates/*.html'],
    },
)
