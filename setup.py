#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="pybatctl",
    version="0.0.1",
    packages=find_packages(),
    author="BetaS (Minsu Kim)",
    author_email="k09089@naver.com",
    description="Python batman-adv(batctl) helper class",
    license="GPLv2",
    keywords="batctl, batman, batman-adv, batmand",
    url="https://github.com/BetaS/pybatctl",
    long_description=open("README.md").read(),
    classifiers=['License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                 'Programming Language :: Python',
                 'Operating System :: POSIX',
                 'Programming Language :: Python :: 2.7'],

)