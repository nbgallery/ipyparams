# vim: expandtab tabstop=4 shiftwidth=4

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='ipyparams',
    version='0.2.0',
    author='Bill Allen',
    author_email='photo.allen@gmail.com',
    description='Send parameters/arguments to notebooks via URL query string parameters.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='jupyter notebook parameters arguments url query'.split(),
    url='https://github.com/nbgallery/ipyparams',
    packages=['ipyparams'],
    package_data={},
    install_requires=[],
    python_requires='>=3.4, <4',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
