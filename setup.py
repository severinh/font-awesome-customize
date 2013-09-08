#!/usr/bin/env python2

from setuptools import setup, find_packages

setup(name='font-awesome-customize',
      version='0.1',
      description='Generate custom versions of Font Awesome',
      long_description=open('README.rst').read(),
      url='https://github.com/severinh/font-awesome-customize',
      author='Severin Heiniger',
      author_email='severinheiniger@gmail.com',
      license='LICENSE',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
          'font-awesome-customize = font_awesome_customize:main',
        ]
      },
      install_requires=['XStatic-Font-Awesome'],
      test_suite='nose.collector',
      tests_require=['nose'])