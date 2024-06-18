# setup.py
from setuptools import setup, find_packages

setup(
    name='my_pyside6_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PySide6',
    ],
    description='A custom PySide6 components library',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_pyside6_library',
)
