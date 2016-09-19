#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import tvdb

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = tvdb.__version__

if sys.argv[-1] == 'publish':
    os.system('cd docs && make html')
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

if sys.argv[-1] == 'test':
    print("Running tests only on current environment.")
    print("Use `tox` for testing multiple environments.")
    os.system('python manage.py test')
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='django-tvdb',
    version=version,
    description="""TVDB support for Django projects""",
    long_description=readme + '\n\n' + history,
    author='Dustyn Gibson',
    author_email='miigotu@gmail.com',
    url='https://github.com/miigotu/django-tvdb',
    packages=[
        'tvdb',
    ],
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    license="GNU General Public License v2 (GPLv2)",
    zip_safe=False,
    keywords='django-tvdb',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)

