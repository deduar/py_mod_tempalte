from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

setup(
    name="basic-template",
    version="0.0.1",
    description="Template library",
    long_description="Template library",
    long_description_content_type="text/markdown",
    url="https://github.com/deduar/py_mod_template",
    author="Eduardo Diez",
    author_email="deduar@gmai.com",
    classifiers=[],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.9",
)
