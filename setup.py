"""
Setup for Magna DAP library
"""

from setuptools import setup, find_packages


with open('README.md',encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE',encoding='utf-8') as f:
    lic = f.read()

setup(
    name='pyTools',
    version='0.0.1',
    description='Mikes PyTools',
    long_description=readme,
    author='Mike Bush',
    author_email='mbush91@gmail.com',
    url='https://github.com/mbush91/mikes-pytools',
    license=lic,
    packages=find_packages(exclude=('tests', 'docs','templates')),
    install_requires=[]
)
