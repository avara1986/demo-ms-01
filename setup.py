# -*- coding: utf-8 -*-
import codecs
import os

import json
from setuptools import setup, find_packages

version = "0.0.1"

if os.path.exists('README.md'):
    long_description = codecs.open('README.md', 'r', 'utf-8').read()
else:
    long_description = ''


install_requires = []
tests_require = []
if os.path.exists('Pipfile.lock'):
    with open('Pipfile.lock') as fd:
        lock_data = json.load(fd)
        install_requires = [
            package_name + package_data['version']
            for package_name, package_data in lock_data['default'].items()
        ]
        tests_require = [
            package_name + package_data['version']
            for package_name, package_data in lock_data['develop'].items()
        ]


setup(
    name="demo",
    version=version,
    description="",
    long_description=long_description,
    classifiers=[
        'Development Status :: {} - In progress'.format(version),
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    license="Proprietary",
    platforms=["any"],
    keywords="",
    url='',
    test_suite='nose.collector',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True
)
