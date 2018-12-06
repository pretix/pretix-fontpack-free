import os
from distutils.command.build import build

from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


setup(
    name='pretix-fontpack-free',
    version='1.1.0',
    description='Pack of free fonts for pretix\' ticket editor',
    long_description=long_description,
    url='https://github.com/pretix/pretix-fontpack-free',
    author='Raphael Michel',
    author_email='mail@raphaelmichel.de',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    entry_points="""
[pretix.plugin]
pretix_fontpackfree=pretix_fontpackfree:PretixPluginMeta
""",
)
