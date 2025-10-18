#!/bin/bash

if [ $# -eq 1 ]; then
    curl -s -I $1 | grep -i Location | cut -d" " -f2
fi


