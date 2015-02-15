#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='mpl_preamble',
    version='0.1.0',
    description="A set of simple matplotlib customisations.",
    long_description=readme + '\n\n' + history,
    author="Kian Ho",
    author_email='hui.kian.ho@googlemail.com',
    url='https://github.com/kianho/mpl_preamble',
    packages=[
        'mpl_preamble',
    ],
    package_dir={'mpl_preamble':
                 'mpl_preamble'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='mpl_preamble',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
