"""Python module/package configuration file.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

# Read the contents of your README file
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    README = f.read()

with open("finpack/VERSION") as version_file:
    version = version_file.read().strip()
assert isinstance(version, str)

install_requirements = []

setup(
    name="finpack",
    version=version,
    py_modules=["finpack"],
    description="Super simple personal finance tracking.",
    long_description=README,
    license="Apache License",
    author="Matt Ferreira",
    author_email="rackreaver@gmail.com",
    download_url="https://github.com/RackReaver/FinPack",
    install_requires=install_requirements,
    packages=find_packages(),
)
