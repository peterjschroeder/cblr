#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='cblr', 
        version='0.1', 
        description='Comic Book List Reader', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/cblr',
        scripts=['cblr'],
        install_requires=['asciimatics', 'fuzzywuzzy', 'natsort', 'python-Levenshtein']
)

