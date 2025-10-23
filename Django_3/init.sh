#!/bin/bash

sudo apk update && sudo apk upgrade
sudo apk add build-base libffi-dev openssl-dev bzip2-dev zlib-dev xz-dev
sudo wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
sudo tar -xvzf Python-3.12.3.tgz

# Change directory without using sudo
cd Python-3.12.3

# Run the following commands with sudo
sudo ./configure
sudo make
sudo make install

# Update the default python3 binary
sudo mv /usr/bin/python3 /usr/bin/python3.bak
sudo ln -s /usr/local/bin/python3.12 /usr/bin/python3

# sudo rm -rf Python-3.12.3
# sudo rm Python-3.12.3.tgz