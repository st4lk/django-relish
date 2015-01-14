import os
from setuptools import setup, find_packages
from relish import __author__, __version__


def __read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


install_requires = __read('requirements.txt').split()

setup(
    name='relish',
    author=__author__,
    author_email='alexevseev@gmail.com',
    version=__version__,
    description='Useful code snippets for django',
    long_description=__read('README.rst'),
    platforms=('Any'),
    packages=find_packages(),
    install_requires=install_requires,
    keywords='django snippet relish'.split(),
    include_package_data=True,
    license='BSD License',
    package_dir={'relish': 'relish'},
    url='https://github.com/st4lk/django-relish',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
