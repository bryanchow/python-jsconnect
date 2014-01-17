import os
from setuptools import setup, find_packages

version = '0.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyjsconnect',
    version = version,
    description = "Python jsConnect client for Vanilla Forums SSO",
    long_description = read('README.rst'),
    classifiers = [],
    keywords = "",
    author = "Bryan Chow",
    author_email = '',
    url = 'https://github.com/bryanchow/python-jsconnect',
    download_url = 'https://github.com/bryanchow/python-jsconnect/tarball/master',
    license = 'BSD',
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
    ],
)
