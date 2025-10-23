#!/bin/bash

python3 -m venv myenv

source myenv/bin/activate

pip --version

# pip install path
pip install git+https://github.com/jaraco/path.git@main