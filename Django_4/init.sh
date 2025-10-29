#!/bin/bash

sudo apk update && sudo apk upgrade && sudo apk add git
sudo apk add --no-cache sqlite-dev
sudo apk add --no-cache gcc musl-dev zlib-dev make
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
sudo apk add --no-cache postgresql-dev gcc python3-dev musl-dev


sudo apk add sqlite-dev
sudo apk add python3-dev gcc musl-dev
sudo ./configure --enable-loadable-sqlite-extensions
sudo make
sudo make install
sudo python3 -c "import sqlite3; print(sqlite3.sqlite_version)"




apk add sqlite sqlite-dev python3-dev gcc musl-dev make
apk del python3
apk add python3

# sudo rm -rf Python-3.12.3
# sudo rm Python-3.12.3.tgz