========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-trusted/badge/?style=flat
    :target: https://readthedocs.org/projects/python-trusted
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/GhostofGoes/python-trusted.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/GhostofGoes/python-trusted

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/GhostofGoes/python-trusted?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/GhostofGoes/python-trusted

.. |requires| image:: https://requires.io/github/GhostofGoes/python-trusted/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/GhostofGoes/python-trusted/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/GhostofGoes/python-trusted/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/GhostofGoes/python-trusted

.. |codecov| image:: https://codecov.io/github/GhostofGoes/python-trusted/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/GhostofGoes/python-trusted

.. |landscape| image:: https://landscape.io/github/GhostofGoes/python-trusted/master/landscape.svg?style=flat
    :target: https://landscape.io/github/GhostofGoes/python-trusted/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/GhostofGoes/python-trusted/badges/gpa.svg
   :target: https://codeclimate.com/github/GhostofGoes/python-trusted
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/trusted.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/trusted

.. |commits-since| image:: https://img.shields.io/github/commits-since/GhostofGoes/python-trusted/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/GhostofGoes/python-trusted/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/trusted.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/trusted

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/trusted.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/trusted

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/trusted.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/trusted


.. end-badges

Bringing "trust but verify" to Python packages

* Free software: MIT license

Installation
============

::

    pip install trusted

Documentation
=============

https://python-trusted.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
