"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Diblo Geo',
    version='0.0.1rc1',
    description='Python Geolocation API',
    long_description=long_description,
    url='https://github.com/pypa/sampleproject',
    author='Henrik Ankersoe',
    author_email='henrik@diblo.dk',
    license='GPL v3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "Programming Language :: Python",
        'Topic :: Software Development :: Build Tools',
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='geocode geocoding geographical maps earth distance bearing',
    packages=find_packages(exclude=['tests*']),
    install_requires=['math'],
)