#!/bin/bash

python3 -m venv local_lib

source local_lib/bin/activate

pip --version

# pip install path
pip install git+https://github.com/jaraco/path.git@main -I --log install.log

python my_program.py 