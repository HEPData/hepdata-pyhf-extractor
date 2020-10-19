# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


# Package meta-data
NAME = "hepdata-pyhf-extractor"
INFO = "Python package to summarize pyhf submissions"
URL = "https://github.com/HEPData/hepdata-pyhf-extractor"
REQUIRES_PYTHON = ">=3.6, <4"
AUTHORS = "HEPData and pyhf teams"
VERSION = open("VERSION", "r").read().strip()


# Installation requirements
INSTALLATION_REQS = []

# Development requirements
DEVELOPMENT_REQS = [
    "black>=20.8b1",
    "coverage>=5.0.4",
    "pre-commit>=2.4.0",
    "pytest>=6.0.2",
    "pytest-cov>=2.10.0",
]


setup(
    name=NAME,
    version=VERSION,
    description=INFO,
    author=AUTHORS,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=INSTALLATION_REQS,
    extras_require={
        "dev": DEVELOPMENT_REQS,
    },
    include_package_data=True,
    license="GPLv2",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    cmdclass={},
)
