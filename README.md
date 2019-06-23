<h1 align="center"> Nomenclate </h1> <br>

<p align="center">
  A tool set for automating and generating strings based on arbitrary user-defined naming conventions
  <a href="http://nomenclate.readthedocs.io/en/latest/">Online Documentation (ReadTheDocs)</a>
</p>

<div align="center">
  <a href="https://readthedocs.org/projects/nomenclate/badge/?version=latest">
    <img src="http://nomenclate.readthedocs.io/en/latest/?badge=latest" alt="Documentation" />
  </a>
  <a href="https://badge.fury.io/py/nomenclate">
    <img src="https://badge.fury.io/py/nomenclate.svg" alt="Build Status" />
  </a>
  <a href="https://circleci.com/gh/AndresMWeber/Nomenclate">
    <img src="https://circleci.com/gh/AndresMWeber/Nomenclate.svg?style=svg" alt="CircleCI Status" />
  </a>
  <a href="https://coveralls.io/github/AndresMWeber/Nomenclate?branch=master">
    <img src="https://coveralls.io/repos/github/AndresMWeber/Nomenclate/badge.svg?branch=master" alt="Code Health" />
  </a>
  <a href="https://landscape.io/github/AndresMWeber/Nomenclate/master">
    <img src="https://landscape.io/github/AndresMWeber/Nomenclate/master/landscape.svg?style=flat" alt="Landscape.io Status" />
  </a>
  <a href="https://pypi.python.org/pypi/nomenclate">
    <img src="https://img.shields.io/pypi/pyversions/nomenclate.svg" alt="PyPI Version" />
  </a>
</div>


Introduction
=============

Nomenclate is a tool which creates persistent objects that can be used to generate strings that follow naming
conventions that you designate.
There are sets of current naming conventions (format strings) that can be replaced or extended following certain rules
for creation. You can add arbitrary tokens as needed and register token filtering of your own designation.

There is a full set of YAML defined suffix/side substitution strings as found in ``env.yml``.
If you want you can create your own .yml file that you will pass to a Nomenclate instance to have your own configuration.

Features
--------
-  Applies a naming convention with arbitrary syntax/grammar to the formatting of string tokens
-  Top down parsing of format string given token-specific grammar rule classes that are extensible
-  Persistent state object instances
-  Up to date with online help docs
-  User-customizable YAML/human-readable config file
-  Easy object property or dictionary state manipulation
-  Cross-Python compatible: Tested and working with Python 2.7 and 3.5
-  Cross-Platform compatible: Works under Linux, Mac OS ,Windows environments
-  Full module/class documentation
-  Sensible token value entry/conversion (like ``side='left'`` with automatic token syntax replacement)

Concept Definitions
-------------------
token
    : A component of the format string which is a meaningful symbol/definition pair that will be filtered by
    a grammar of regular expressions.
    A simplified representation could be token=value wherein the token (as found in the format string) will be resolved
    to the value as is adheres to the token's syntax/grammar rules

format string
    : A string that represents a series of tokens separated with arbitrary delimiters.

    e.g. - ``side_location_nameDecoratorVar_childtype_purpose_type``

    Note: Nomenclate automatically supports camelCasing the tokens to separate them as a natural delimiter.

`For a review of parsing/composition look here <https://en.wikipedia.org/wiki/Parsing>`_

Installation
============
#### Windows, etc.

A universal installation method (that works on Windows, Mac OS X, Linux, ..., and always provides the latest version) is to use `pip`:

.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools
    $ pip install nomenclateAPI


Usage
=====
#### Python Package Usage

Use this tool via package level functions

.. code-block:: python

    nada

Version Support
===============
Currently this package supports Python 2.7, 3.5 and 3.6

Acknowledgments
===============

Attribution
===========
