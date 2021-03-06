#!/usr/bin/python

from setuptools import setup


setup(
    name='telephus',
    version='1.0.0',
    description=('connection pooled, low-level client API for Cassandra in '
                 'Twisted (Python)'),
    author='brandon@faltering.com',
    url='http://github.com/driftx/Telephus',
    packages=['telephus',
              'telephus.cassandra'],
    install_requires=[
        'Twisted==13.0',
        'thrift>=0.9.1',
        'blist==1.3.6',
        'pure-sasl>=0.1.5',
    ],
)
