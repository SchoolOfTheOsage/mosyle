from setuptools import find_packages, setup

setup(
    name="mosyle",
    version="0.0.3",
    description="Mosyle Manager Python API",
    author="Nathan McGuire",
    author_email="mcguiren@osageschools.org",
    url="https://github.com/SchoolOfTheOsage/mosyle",
    packages=find_packages(),
    install_requires=["requests"],
)
