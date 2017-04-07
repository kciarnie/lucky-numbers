# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

requires = ['bumpversion', 'click']
tests_require = ['pytest', 'pytest-cache', 'pytest-cov', 'configparser']


class PyTest(TestCommand):
    def __init__(self):
        self.test_suite = True
        self.test_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = True
        self.test_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="lucky numbers",
    author="Kevin Ciarniello",
    author_email="kciarnie@gmail.com",
    version="0.0.1",
    description="This is the lucky number series",
    long_description="\n\n".join([open("README.rst").read()]),
    license='MIT',
    url="https://github.com/kciarnie/lucky-numbers.git",
    packages=find_packages(),
    install_requires=requires,
    entry_points={'console_scripts': [
        'luckynum = luckynumber:main'
    ]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'],
    extras_require={'test': tests_require},
    cmdclass={'test': PyTest}
)
