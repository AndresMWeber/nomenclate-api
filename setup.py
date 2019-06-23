import codecs
import os
import re
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

name = 'nomenclateAPI'
__version__ = '0.0.0'

with codecs.open(os.path.abspath(os.path.join(name, 'version.py'))) as ver_file:
    version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(version_regex, ver_file.read(), re.M)
    try:
        __version__ = mo.group(1)
    except AttributeError:
        raise IOError('Could not find version in %s' %
                      os.path.join(name, 'version.py'))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('GIT_TAG')
        if __version__ not in tag:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, __version__)
            sys.exit(info)


setup(
    name=name,
    version=__version__,
    url='https://github.com/andresmweber/nomenclate-api',
    author='Andres Weber',
    author_email='andresmweber@gmail.com',
    description='A tool for generating strings based on a preset naming convention.',
    long_description="`Online Documentation (ReadTheDocs) <http://nomenclate.readthedocs.io/en/latest/>`_",
    keywords='naming conventions labels config convention name parsing parse',
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    package_data={},
    include_package_data=True,
    test_suite='tests',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation :: Sphinx'
    ],
    install_requires=[
        'six'
    ],
    extras_require={
        'tests': [
            'coverage',
            'coveralls',
            'unittest2',
            'nose2'
        ],
        'dev': [
            'twine',
            'Sphinx',
            'docutils',
            'docopt'
        ]
    },
    cmdclass={
        'verify': VerifyVersionCommand
    },
    license='MIT',
)
