#!/bin/bash

# Build for windowns amd64
python setup.py bdist_wheel --plat-name=win-amd64

# Build for linux amd64
python setup.py sdist bdist_wheel
