# -*- coding: utf-8 -*-

"""Top-level package for Weirwood PyFinance."""

__author__ = "Alex Encalado Masia"
__email__ = "encalado.masia@gmail.com"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0.0.0"


def get_module_version():
    return __version__


from .finten import FinTen
