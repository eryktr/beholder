import setuptools
from pathlib import Path

from setuptools import find_namespace_packages

long_description = Path("README.md").read_text()

setuptools.setup(
    name="beholderteam-beholder",
    version="0.1.0",
    author="beholder-devteam",
    maintainer="beholder_devteam",
    description="A simple tool to monitor selected websites",
    long_description=long_description,
    packages=find_namespace_packages(include=('beholder', 'beholder.*')),
    install_requires=(
        'requests==2.23.0',
    ),
    extras_require={
        'dev': (
            'attrs==19.3.0',
            'beautifulsoup4==4.9.0',
            'coverage==5.0.4',
            'entrypoints==0.3',
            'flake8==3.8.0a1',
            'flake8-commas==2.0.0',
            'lxml==4.5.0',
            'mccabe==0.6.1',
            'more-itertools==8.2.0',
            'mypy==0.770',
            'mypy-extensions==0.4.3',
            'packaging==20.3',
            'pluggy==0.13.1',
            'py==1.8.1',
            'pycodestyle==2.6.0a',
            'pyflakes==2.2.0',
            'pyparsing==2.4.6',
            'pytest==5.4.1',
            'pytest-mock==2.0.0',
            'pytest-cov==2.8.1',
            'mypy==0.770',
            'six==1.14.0',
            'typed-ast==1.4.1',
            'typing-extensions==3.7.4.1',
            'wcwidth==0.1.9',
        ),
    },
    python_requires='>=3.8.0',
)
