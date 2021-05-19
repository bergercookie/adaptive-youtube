# -*- coding:utf-8 -*-

import setuptools
from sphinxext import adaptive_youtube as pkg

pkgname = pkg.__name__

__pkgname__ = "sphinxext.adaptive_youtube"
__version__ = "0.0.2"
__author__ = "@john_sane"
__license__ = "LGPLv3"

setuptools.setup(
    name=__pkgname__,
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=["sphinx"],
    author=__author__,
    license=__license__,
    url="https://github.com/john-sane/adaptive-youtube",
    description="""embedding gist to sphinx""",
    long_description=__doc__,
    namespace_packages=["sphinxext"],
    classifiers="""
Programming Language :: Python
Development Status :: 4 - Beta
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.7
Topic :: Software Development :: Documentation
""".strip().splitlines(),
)
