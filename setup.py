#!/usr/bin/python

from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

README = path.abspath(path.join(path.dirname(__file__), 'README.rst'))
desc = 'A Python logging handler for Fluentd event collector'

setup(
    name='logsense-fluent-logger',
    version='0.0.6',
    description=desc,
    long_description=open(README).read(),
    package_dir={'logsensefluent': 'fluent'},
    packages=['logsensefluent'],
    install_requires=['msgpack'],
    url='https://github.com/collectivesense/fluent-logger-python',
    download_url='http://pypi.python.org/pypi/logsense-fluent-logger/',
    license='Apache License, Version 2.0',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 5 - Production/Stable',
        'Topic :: System :: Logging',
        'Intended Audience :: Developers',
    ],
    python_requires=">=2.7,!=3.0,!=3.1,!=3.2,!=3.3,<3.8",
    test_suite='tests')
