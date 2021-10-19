#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "black",
    "codecov",
    "flake8",
    "flake8-debugger",
    "pytest",
    "pytest-cov",
    "pytest-raises",
    "python-dotenv"
]

dev_requirements = [
    *setup_requirements,
    *test_requirements,
    "bump2version",
    "coverage",
    "ipython",
    "m2r2",
    "pytest-runner",
    "Sphinx",
    "sphinx_rtd_theme",
    "tox",
    "twine",
    "wheel",
]

requirements = ["yfinance","pandas","httpretty"]

extra_requirements = {
    "setup": setup_requirements,
    "test": test_requirements,
    "dev": dev_requirements,
    "all": [
        *requirements,
        *dev_requirements,
    ]
}

setup(
    author="Alex Encalado Masia",
    author_email="encalado.masia@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Python API for downloading stock prices and fundamental accounting concepts",
    entry_points={
        "console_scripts": [
            "my_example=weirwood_pyfinance.bin.my_example:main"
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="weirwood_pyfinance",
    name="weirwood_pyfinance",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    #python_requires=">3.5",
    setup_requires=setup_requirements,
    test_suite="weirwood_pyfinance/tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url="https://github.com/weirwoodai/weirwood_pyfinance",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="0.0.2",
    zip_safe=False,
)
