#!/usr/bin/python

from distutils.core import setup


setup(
    name='telephus',
    version='1.0.0~beta1',
    description=('connection pooled, low-level client API for Cassandra in '
                 'Twisted (Python)'),
    author='brandon@faltering.com',
    url='http://github.com/driftx/Telephus',
    packages=['telephus',
              'telephus.cassandra'],
    requires=[
        'Twisted (==13.0)',
        'thrift (>=0.9.1)',
        'blist (==1.3.6)',
        'puresasl (>=0.1.5)',
    ],
)
