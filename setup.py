#!/usr/bin/env python

from setuptools import setup

setup(
    name='notsouid',
    version='0.0.2',
    description='not so unique ids',
    author='Nic West',
    author_email='oss@nicwest.com',
    url='https://github.com/nicwest/notsouid',
    packages=['notsouid'],
    install_requires=[
        'mock>=2.0.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)
