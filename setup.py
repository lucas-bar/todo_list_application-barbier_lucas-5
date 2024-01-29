#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.core import setup
setup(
    name='todo_list_application_barbier_lucas_5',
    version='1.0',
    author='Lucas Barbier',
    license='MIT',
    description='A console-based application to help keep track of tasks.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo_list_application = main:main',  # Remplacez 'main' par le nom de votre fichier principal
        ],
    },
    install_requires=[
        # Liste des dépendances, le cas échéant
    ],
)

