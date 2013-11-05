#  -*- coding: utf-8 -*- 
"""
Setup tools script for adaptive lab project.
"""

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

def required(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().split('\n')

config = {
    "name" : "adaptivelab",
    "version" : "0.0.1",
    "namespace_packages" : ['adaptivelab'],
    "packages" : find_packages(exclude=[
                                         "*.tests", "*.tests.*", "tests.*", "tests",
                                         "*.ez_setup", "*.ez_setup.*", "ez_setup.*", "ez_setup",
                                         "*.examples", "*.examples.*", "examples.*", "examples",
                                         "*.testpages", "*.testpages.*", "testpages.*", "testpages",
                                       ]),
    "include_package_data" : True,
    "package_data" : { },
    "scripts" : [ ],
    "entry_points" : { },
    "install_requires" : [  required('../install-requires.txt') ],
    "tests_require" : [ required('../install-test-requires.txt') ],
    "test_suite" : 'nose.collector',
    "zip_safe" : False,
    
    # Metadata for upload to PyPI
    "author" : 'Matthew Green',
    "author_email" : "matthew@newedgeengineering.com",
    "description" : "Technical Test",
    "long_description" : "",
    "classifiers" : [
                      "Programming Language :: Python",
                    ],
    "license" : "",
    "keywords" : "",
    "url" : "",
}

setup(**config)
